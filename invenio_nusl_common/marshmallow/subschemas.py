from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow import validates, ValidationError
from marshmallow.fields import List, URL, Nested, Url, Boolean, Integer, Date
from marshmallow.validate import Length
from oarepo_multilingual.marshmallow import MultilingualStringV2
from oarepo_taxonomies.marshmallow import TaxonomyField

from invenio_nusl_common.marshmallow.fields import ISBN, ISSN, DOI, RIV, Year


class TitledMixin:
    title = MultilingualStringV2()


class RelatedURISchema(StrictKeysMixin):
    coar = SanitizedUnicode()
    eprint = SanitizedUnicode()
    vocabs = SanitizedUnicode()


class AccessRightsMixin:
    relatedURI = Nested(RelatedURISchema)


class FunderMixin:
    funderISVaVaICode = SanitizedUnicode()


class RelatedIDSchema(StrictKeysMixin):
    RID = SanitizedUnicode()
    DOI = DOI()
    ISVaVaI = SanitizedUnicode()


class InstitutionsMixin:
    relatedID = Nested(RelatedIDSchema)
    aliases = List(SanitizedUnicode())
    ico = SanitizedUnicode()
    url = Url()
    provider = Boolean(missing=False)
    formerNames = List(SanitizedUnicode())


class CountryCodeSchema(StrictKeysMixin):
    aplha2 = SanitizedUnicode(validate=Length(equal=2))
    aplha3 = SanitizedUnicode(validate=Length(equal=3))


class CountryMixin:
    numericCode = Integer()
    code = Nested(CountryCodeSchema)

    @validates(numericCode)
    def validate_length(self, value):
        if len(str(value)) != 3:
            raise ValidationError("Numeric code must to be three character lenght.")


class RightsRelated(StrictKeysMixin):
    uri = URL()


class RightsMixin:
    icon = Url()
    related = Nested(RightsRelated)


class SeriesMixin:
    name = SanitizedUnicode(required=True)
    volume = SanitizedUnicode(required=True)


class SubjectMixin:
    relatedURI = List(Url)
    DateCreated = Date()
    DateRevised = Date()
    DateEstablished = Date()


class PSHMixin:
    altLabel = MultilingualStringV2()


class CZMeshMixin:
    TreeNumberList = List(SanitizedUnicode())


class MedvikMixin:
    pass


class PersonSchema(StrictKeysMixin):
    name = SanitizedUnicode(required=True)
    ORCID = SanitizedUnicode()
    scopusID = SanitizedUnicode()
    researcherID = SanitizedUnicode()  # WOS ID
    czenasAutID = SanitizedUnicode()
    vedidk = SanitizedUnicode()
    institutionalID = SanitizedUnicode()  # TODO: vložit prefix instituce


class ContributorMixin:
    dataCiteCode = SanitizedUnicode()
    marcCode = SanitizedUnicode()


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


class WorkIdentifersSchema(StrictKeysMixin):
    isbn = List(ISBN())
    issn = List(ISSN())
    doi = DOI()
    RIV = RIV()


class FundingReferenceSchema(StrictKeysMixin):
    projectID = SanitizedUnicode()
    projectName = SanitizedUnicode()
    fundingProgram = SanitizedUnicode()
    funder = TaxonomyField(mixins=[FunderMixin, TitledMixin])


class PublicationPlaceSchema(StrictKeysMixin):
    place = SanitizedUnicode()
    country = TaxonomyField(mixins=[CountryMixin])


class RelatedItemSchema(StrictKeysMixin):
    itemTitle = MultilingualStringV2(required=True)
    itemDOI = DOI()
    itemISBN = ISBN()
    itemISSN = ISSN()
    itemURL = URL()
    itemYear = Year()
    itemVolume = SanitizedUnicode()
    itemIssue = SanitizedUnicode()
    itemStartPage = SanitizedUnicode()
    itemEndPage = SanitizedUnicode()
    # itemRelationship = # TODO: zeptat se Péti až bude OK
