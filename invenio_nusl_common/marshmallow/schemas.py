from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow.fields import List, URL, Integer
from marshmallow.validate import Length
from oarepo_multilingual.marshmallow import MultilingualStringV2
from oarepo_taxonomies.marshmallow import TaxonomyField

from invenio_nusl_common.marshmallow.fields import ISBN, ISSN, DOI, RIV, Year
from invenio_nusl_common.marshmallow.mixins import ContributorMixin, FunderMixin, TitledMixin, \
    CountryMixin


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


class workIdentifersSchema(StrictKeysMixin):
    isbn = List(ISBN())
    issn = List(ISSN())
    doi = DOI()
    RIV = RIV()


class fundingReferenceSchema(StrictKeysMixin):
    projectID = SanitizedUnicode()
    projectName = SanitizedUnicode()
    fundingProgram = SanitizedUnicode()
    funder = TaxonomyField(mixins=[FunderMixin, TitledMixin])


class RelatedIDSchema(StrictKeysMixin):
    RID = SanitizedUnicode()
    DOI = DOI()
    ISVaVaI = SanitizedUnicode()


class RightsRelated(StrictKeysMixin):
    uri = URL()


class CountryCodeSchema(StrictKeysMixin):
    aplha2 = SanitizedUnicode(validate=Length(equal=2))
    aplha3 = SanitizedUnicode(validate=Length(equal=3))


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


class RelatedUriCZMesh(StrictKeysMixin):
    medvik = URL()
    Mesh = URL()
