# # -*- coding: utf-8 -*-
# #
# # Copyright (C) 2019 CERN.
# #
# # My site is free software; you can redistribute it and/or modify it under
# # the terms of the MIT License; see LICENSE file for more details.
#
# """JSON Schemas."""
#
from __future__ import absolute_import, print_function

from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow import post_load, ValidationError
from marshmallow.fields import Nested, Url, Boolean, List
from marshmallow.validate import Length
from oarepo_invenio_model.marshmallow import InvenioRecordMetadataSchemaV1Mixin
from oarepo_multilingual.marshmallow import MultilingualStringV2
from oarepo_taxonomies.marshmallow import TaxonomyField

from nr_common.marshmallow.fields import NRDate
from nr_common.marshmallow.subschemas import PersonSchema, ContributorSchema, \
    WorkIdentifersSchema, FundingReferenceSchema, PublicationPlaceSchema, RelatedItemSchema, \
    TitledMixin, AccessRightsMixin, InstitutionsMixin, RightsMixin, SeriesMixin, SubjectMixin, \
    PSHMixin, CZMeshMixin, MedvikMixin, RecordIdentifier


#


class CommonMetadataSchemaV2(InvenioRecordMetadataSchemaV1Mixin, StrictKeysMixin):
    """Schema for the record metadata."""

    abstract = MultilingualStringV2()
    accessibility = MultilingualStringV2()
    accessRights = TaxonomyField(mixins=[TitledMixin, AccessRightsMixin], required=True)
    creator = List(Nested(PersonSchema), required=True)
    contributor = List(Nested(ContributorSchema))
    dateIssued = NRDate(required=True)
    dateModified = NRDate()
    resourceType = TaxonomyField(mixins=[TitledMixin], required=True)
    extent = SanitizedUnicode()  # TODO: pokud nemáme extent, spočítat z PDF - asi nepůjde
    externalLocation = Url()
    control_number = SanitizedUnicode(required=True)
    recordIdentifiers = Nested(RecordIdentifier)
    workIdentifiers = Nested(WorkIdentifersSchema)
    isGL = Boolean()
    language = TaxonomyField(mixins=[TitledMixin], required=True)
    note = List(SanitizedUnicode())
    fundingReference = List(Nested(FundingReferenceSchema))
    provider = TaxonomyField(mixins=[TitledMixin, InstitutionsMixin], required=True)
    entities = TaxonomyField(mixins=[TitledMixin, InstitutionsMixin], many=True)
    publicationPlace = Nested(PublicationPlaceSchema)
    publisher = SanitizedUnicode()
    relatedItem = List(Nested(RelatedItemSchema))
    rights = TaxonomyField(mixins=[TitledMixin, RightsMixin])
    series = TaxonomyField(mixins=[SeriesMixin])
    subject = TaxonomyField(mixins=[TitledMixin, SubjectMixin, PSHMixin, CZMeshMixin, MedvikMixin],
                            many=True)
    keywords = List(MultilingualStringV2())
    title = List(MultilingualStringV2(required=True), required=True, validate=Length(min=1))
    titleAlternate = List(MultilingualStringV2())

    @post_load
    def validate_keywords_subjects(self, data, **kwargs):
        subject = [x for x in data.get("subject", []) if not x["is_ancestor"]]
        keywords = data.get("keywords", [])
        if len(keywords) + len(subject) < 3:
            raise ValidationError("At least three subjects or keyword are required")
        return data

    @post_load
    def copy_to_entities(self, data, **kwargs):
        entities = data.get("entities")
        if not entities:
            data["entities"] = data["provider"]
        return data
