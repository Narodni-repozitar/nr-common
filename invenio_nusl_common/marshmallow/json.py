# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

import os
from functools import lru_cache
from json import load

from invenio_records_rest.schemas import Nested, StrictKeysMixin
from flask_taxonomies.marshmallow import TaxonomySchemaV1
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


def validate_bterm(bterm, json_path):  # TODO Součást třídy, vypadá to lépe
    terms = import_json(json_path)  # TODO: vyměnit za relativní
    if terms.get(bterm, "unknown") == "unknown":
        raise ValidationError('The chosen broader term is not valid.')


def validate_term(bterm, term, json_path):  # TODO Součást třídy, vypadá to lépe
    if term is not None:
        terms = import_json(json_path)
        if bterm not in terms:
            raise ValidationError('The chosen bterm is not valid.')
        if term not in terms[bterm]:
            raise ValidationError('The chosen term is not valid.')


def validate_nusl_bterm(bterm):
    validate_bterm(bterm,
                   os.path.join(os.path.dirname(__file__), "data", "document_typology_NUSL.json"))


def validate_nusl_term(bterm, term):
    validate_term(bterm, term,
                  os.path.join(os.path.dirname(__file__), "data", "document_typology_NUSL.json"))


def validate_RIV_bterm(bterm):
    validate_bterm(bterm,
                   os.path.join(os.path.dirname(__file__), "data", "document_typology_RIV.json"))


def validate_RIV_term(term):
    validate_term(term,
                  os.path.join(os.path.dirname(__file__), "data", "document_typology_RIV.json"))


########################################################################
#                            SCHEMAS                                   #
########################################################################
def createValueTypeSchemaV1():
    class ValueTypeSchemaV1(StrictKeysMixin):
        """Ids schema."""

        type = SanitizedUnicode(required=True, allow_none=True)
        value = SanitizedUnicode(required=True, allow_none=True)

    return ValueTypeSchemaV1


def createMultilanguageSchemaV1():
    class MultilanguageSchemaV1(StrictKeysMixin):
        """ """

        name = SanitizedUnicode(required=True)
        lang = fields.String(validate=validate_language,
                             required=True)

        @pre_load
        def change_lang_code(self, data):
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

    return MultilanguageSchemaV1


def createDoctypeSubSchemaV1():
    class DoctypeSubSchemaV1(TaxonomySchemaV1):
        pass

    return DoctypeSubSchemaV1


def createNUSLDoctypeSchemaV1():
    class NUSLDoctypeSchemaV1(StrictKeysMixin):
        bterm = SanitizedUnicode(required=True)
        term = SanitizedUnicode(required=True)

        @pre_load
        def validate_taxonomy(self, data):
            validate_nusl_term(data["bterm"], data["term"])

    return NUSLDoctypeSchemaV1


def createRIVDoctypeSchemaV1():
    class RIVDoctypeSchemaV1(StrictKeysMixin):
        bterm = SanitizedUnicode(required=True, validate=validate_RIV_bterm)
        term = SanitizedUnicode(validate=validate_RIV_term, allow_none=True)

        @post_load
        def isPartOf(self, data):
            if "term" in data:
                term = data["term"]
                bterm = data["bterm"]
                terms = import_json(
                    "/home/semtex/Projekty/nusl/invenio-nusl-common/invenio_nusl_common/marshmallow/data/document_typology_RIV.json")  # TODO: vyměnit za relativní
                if terms[bterm] is not None:
                    if term not in terms[bterm]:
                        raise ValidationError("The term is not part of broader term")

    return RIVDoctypeSchemaV1


def createOrganizationSchemaV1():
    class OrganizationSchemaV1(StrictKeysMixin):
        """ """

        id = Nested(createValueTypeSchemaV1())
        address = SanitizedUnicode()
        contactPoint = fields.Email(required=False)
        name = Nested(createMultilanguageSchemaV1())
        url = fields.Url()
        provider = fields.Boolean()
        isPartOf = fields.List(SanitizedUnicode())

    return OrganizationSchemaV1
