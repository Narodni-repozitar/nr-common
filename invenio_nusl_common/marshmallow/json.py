# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from audioop import max

from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import DateString, \
    PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, missing, validate, pre_load, post_load
from pycountry import languages
from marshmallow import ValidationError


########################################################################
#                 VALIDATION MODELS                                    #
########################################################################

def validate_language(lang):
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
                         required=True)  # TODO: velikost písmen, automaticky přepsat CES na CZE, DEU na GER

    @post_load
    def change_lang_code(self, data):
        lang = data["lang"].lower()
        alpha3 = languages.get(alpha_3=lang)
        if alpha3 is not None:
            try:
                data["lang"] = alpha3.bibliographic
                return data
            except AttributeError:
                return data
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
