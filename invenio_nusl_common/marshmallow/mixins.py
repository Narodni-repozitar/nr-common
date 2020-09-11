from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow import ValidationError, validates
from marshmallow.fields import Nested, List, Url, Boolean, Integer, DateTime, Date
from oarepo_multilingual.marshmallow import MultilingualStringV2

from invenio_nusl_common.marshmallow.schemas import RelatedIDSchema, CountryCodeSchema, \
    RightsRelated, RelatedUriCZMesh


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


class FunderMixin:
    funderISVaVaICode = SanitizedUnicode()


class InstitutionsMixin:
    relatedID = Nested(RelatedIDSchema)
    aliases = List(SanitizedUnicode())
    ico = SanitizedUnicode()
    url = Url()
    provider = Boolean(missing=False)
    formerNames = List(SanitizedUnicode())


class CountryMixin:
    numericCode = Integer()
    code = Nested(CountryCodeSchema)

    @validates(numericCode)
    def validate_length(self, value):
        if len(str(value)) != 3:
            raise ValidationError("Numeric code must to be three character lenght.")


class RightsMixin:
    icon = Url()
    related = Nested(RightsRelated)


class SeriesMixin:
    name = SanitizedUnicode(required=True)
    volume = SanitizedUnicode(required=True)


class PSHMixin:
    modified = DateTime()
    uri = Url()
    altLabel = MultilingualStringV2()


class CZMeshMixin:
    relatedURI = Nested(RelatedUriCZMesh)
    DateCreated = Date()
    DateRevised = Date()
    DateEstablished = Date()
    TreeNumberList = List(SanitizedUnicode())


class MedvikMixin:
    relatedURI = List(Nested(RelatedUriCZMesh))
