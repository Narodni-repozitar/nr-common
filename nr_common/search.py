from typing import List

from elasticsearch_dsl import Q
from flask import current_app


def nr_query_parser(qstr: str = None):
    """Docs for query_string: https://www.elastic.co/guide/en/elasticsearch/reference/current
    /query-dsl-query-string-query.html"""
    languages = current_app.config.get("MULTILINGUAL_SUPPORTED_LANGUAGES", ["cs", "en"])
    fields = current_app.config.get("NR_SEARCH_FIELDS", [])
    new_fields = []
    for field in fields:
        expanded = replace_language_placeholder(field, languages)
        new_fields.extend(expanded)
    fields = new_fields
    assert isinstance(fields, list), f"NR_SEARCH_FIELDS must be list, not {type(fields)}"
    if qstr:
        if fields:
            return Q('query_string', query=qstr, fields=fields)
        else:
            return Q('query_string', query=qstr)
    return Q()


def replace_language_placeholder(field: str, languages: List[str]) -> List[str]:
    if "*" not in field:
        return [field]
    res = []
    for lang in languages:
        res.append(field.replace('*', lang))
    return res
