from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow.fields import Nested
from oarepo_multilingual.marshmallow import MultilingualStringV2
from oarepo_taxonomies.marshmallow import TaxonomyField


# MIXINS

class TitledMixin:
    title = MultilingualStringV2()


class RelatedURISchema(StrictKeysMixin):
    coar = SanitizedUnicode()
    eprint = SanitizedUnicode()
    vocabs = SanitizedUnicode()


class AccessRightsMixin:
    relatedURI = Nested(RelatedURISchema)


class ContributorMixin:
    dataCiteCode = SanitizedUnicode()
    marcCode = SanitizedUnicode()


# SCHEMAS

class PersonSchema(StrictKeysMixin):
    name = SanitizedUnicode(required=True)
    ORCID = SanitizedUnicode()
    scopusID = SanitizedUnicode()
    researcherID = SanitizedUnicode()  # WOS ID
    czenasAutID = SanitizedUnicode()
    vedidk = SanitizedUnicode()
    institutionalID = SanitizedUnicode()  # TODO: vložit prefix instituce


class ContributorSchema(PersonSchema):
    role = TaxonomyField(mixins=[ContributorMixin])


class RecordIdentifier(StrictKeysMixin):
    pass
    # nuslOAI =
    # nrcrHandle
    # nrcrOAI
    # originalRecord
    # originalRecordOAI
    # catalogueSysNo


class workIdentifers(StrictKeysMixin):
    isbn
    issn
    doi
    RIV
