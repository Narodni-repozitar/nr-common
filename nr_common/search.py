import json
from functools import lru_cache
from typing import List

from elasticsearch_dsl import Q
from flask import current_app
from invenio_search import current_search
from luqum.elasticsearch import SchemaAnalyzer, ElasticsearchQueryBuilder
from luqum.parser import parser
from luqum.tree import Word


def nr_query_parser(qstr: str = None, index_name: str = None, enpoint_name: str = None):
    if not qstr:
        return Q()
    tree = parser.parse(qstr)
    if isinstance(tree, Word):
        return nr_simple_query_parser(qstr)
    return nr_luqum_query_parser(tree, mapping)


def nr_simple_query_parser(qstr: str = None):
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
    if fields:
        return Q('query_string', query=qstr, fields=fields)
    else:
        return Q('query_string', query=qstr)


def nr_luqum_query_parser(tree, mapping):
    mapping = get_mapping(mapping)  # TODO: vyřešit jak brát mapping z requestu
    schema_analyzer = SchemaAnalyzer(mapping)
    q_builder_opt = schema_analyzer.query_builder_options()  # TODO: využít i v simple query parser
    es_builder = ElasticsearchQueryBuilder(**q_builder_opt)
    query = es_builder(tree)
    return Q(query)


@lru_cache(maxsize=20)
def get_mapping(mapping: str = "nr_common-nr-common-v1.0.0") -> dict:
    mapping_path = current_search.mappings.get(mapping)
    with open(mapping_path, "r") as f:
        return json.load(f)


def replace_language_placeholder(field: str, languages: List[str]) -> List[str]:
    if "*" not in field:
        return [field]
    res = []
    for lang in languages:
        res.append(field.replace('*', lang))
    return res
