# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow import fields, pre_load, ValidationError
from pycountry import languages


########################################################################
#                 VALIDATION MODELS                                    #
########################################################################

def validate_language(lang):  # TODO: zkontrolovat jen alpha3 a nejdřív bib
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

    type = SanitizedUnicode()
    value = SanitizedUnicode(required=True)


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


class OrganizationSchemaV1(StrictKeysMixin):  # TODO: Dodělat
    """ """

    id = SanitizedUnicode()
    address = SanitizedUnicode()
    contactPoint = fields.Email()
    name = Nested(MultilanguageSchemaV1)
    url = fields.Url()
    provider = fields.Boolean()
    isPartOf = fields.List(SanitizedUnicode())
