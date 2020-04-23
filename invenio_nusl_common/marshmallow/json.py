# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from copy import deepcopy
from functools import lru_cache
from json import load
from urllib.parse import urlparse

from flask_taxonomies.jsonresolver import get_taxonomy_term
from flask_taxonomies.marshmallow import TaxonomySchemaV1
from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow import fields, pre_load, ValidationError, post_load
from pycountry import languages



@lru_cache()
def import_json(path: str):
    json_file = open(path, 'r')
    json_dict = load(json_file)
    return json_dict


########################################################################
#                 VALIDATION MODELS                                    #
########################################################################

def validate_language(lang):  # TODO: zkontrolovat jen alpha3 a nejdřív bib, součást třídy
    lang = lang.lower()
    alpha3 = languages.get(alpha_3=lang)
    bib = languages.get(bibliographic=lang)
    if alpha3 is None and bib is None:
        raise ValidationError('The language code is not part of ISO-639 codes.')


########################################################################
#                            SCHEMAS                                   #
########################################################################

class ValueTypeSchemaV1(StrictKeysMixin):
    """Ids schema."""

    type = SanitizedUnicode(required=True, allow_none=True)
    value = SanitizedUnicode(required=True, allow_none=True)


class MultilanguageSchemaV1(StrictKeysMixin):
    """ """

    name = SanitizedUnicode(required=True)
    lang = fields.String(validate=validate_language,
                         required=True)

    @pre_load
    def change_lang_code(self, data, **kwargs):
        if "lang" in data:
            lang = data["lang"].lower()
            if languages.get(alpha_3=lang) is not None:
                language = languages.get(alpha_3=lang)
            elif languages.get(alpha_2=lang):
                language = languages.get(alpha_2=lang)
            elif languages.get(bibliographic=lang):
                language = languages.get(bibliographic=lang)
            else:
                language = None
            if hasattr(language, "bibliographic"):
                data["lang"] = language.bibliographic
            elif hasattr(language, "alpha_3"):
                data["lang"] = language.alpha_3
            else:
                pass
        return data


class ApprovedTaxonomySchema(TaxonomySchemaV1):
    approved = fields.Boolean(missing=False)
    date_of_serialization = fields.DateTime()
    taxonomy = SanitizedUnicode()

    @post_load()
    def subject_or_keyword_required(self, data, **kwargs):
        if "$ref" in data.keys():
            ref = data["$ref"]
            url = urlparse(data["$ref"])
            path_array = [x for x in url.path.split("/") if len(x) > 0]
            slug = path_array[-1]
            code = path_array[path_array.index("taxonomies") + 1]
            data_ = get_taxonomy_term(code=code, slug=slug)
            data = {"$ref": ref}
        else:
            data_ = deepcopy(data)
        if not data_.get("approved"):
            raise ValidationError("The taxonomy has not been approved by curator, yet.")
        return data


class DoctypeSubSchemaV1(ApprovedTaxonomySchema):
    pass


class OrganizationSchemaV1(StrictKeysMixin):
    """ """

    id = Nested(ValueTypeSchemaV1())
    address = SanitizedUnicode()
    contactPoint = fields.Email(required=False)
    name = Nested(MultilanguageSchemaV1())
    url = fields.Url()
    provider = fields.Boolean()
    isPartOf = fields.List(SanitizedUnicode())
