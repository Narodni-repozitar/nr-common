from datetime import datetime

import pytest
from marshmallow import ValidationError

from invenio_nusl_common.marshmallow import CommonMetadataSchemaV2


def test_required_fields(app, db, taxonomy_tree, base_json, base_json_dereferenced):
    schema = CommonMetadataSchemaV2()
    json = base_json
    result = schema.load(json)
    assert result == base_json_dereferenced


class TestAbstract:
    def test_abstract_load_1(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        abstract_ = {
            "cs": "Testovací abstrakt",
            "en": "Test abstract"
        }
        base_json["abstract"] = abstract_
        base_json_dereferenced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_abstract_load_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        abstract_ = [{
            "cs": "Testovací abstrakt",
            "en": "Test abstract"
        }]
        base_json["abstract"] = abstract_
        base_json_dereferenced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_abstract_load_3(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        abstract_ = {
            "cs": "Testovací abstrakt",
            "pl": "Test abstract"
        }
        base_json["abstract"] = abstract_
        base_json_dereferenced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_abstract_load_4(self, db, taxonomy_tree, base_json, base_json_dereferenced):
        abstract_ = {
            "cze": "Testovací abstrakt",
            "en": "Test abstract"
        }
        base_json["abstract"] = abstract_
        base_json_dereferenced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestAccessibility:
    def test_accessibility(self, db, taxonomy_tree, base_json, base_json_dereferenced):
        acc_ = {
            "cs": "Dostupné kdesi blabla",
            "en": "Avallable at blabla"
        }
        base_json["accessibility"] = acc_
        base_json_dereferenced["accessibility"] = acc_
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_accessibility_2(self, db, taxonomy_tree, base_json, base_json_dereferenced):
        acc_ = [
            {
                "value": "Dostupné kdesi blabla",
                "lang": "cz"
            },
            {
                "value": "Avallable at blabla",
                "lang": "en"
            }
        ]
        base_json["accessibility"] = acc_
        base_json_dereferenced["accessibility"] = acc_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestAccessRights:
    def test_access_rights_1(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        ar = {
        }
        base_json["accessRights"] = ar
        base_json_dereferenced["accessRights"] = ar
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_access_rights_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        ar = [{
        }]
        base_json["accessRights"] = ar
        base_json_dereferenced["accessRights"] = ar
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_access_rights_3(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        ar = [{
            "links": {
                "self": "bla"
            }
        }]
        base_json["accessRights"] = ar
        base_json_dereferenced["accessRights"] = ar
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValueError):
            schema.load(base_json)


class TestCreator:
    def test_creator(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = [{
            "name": "Daniel Kopecký",
            "ORCID": "125456",
            "scopusID": "125456",
            "researcherID": "125456",
            "czenasAutID": "125456",
            "institutionalID": "vscht123456"
        }]
        field = "creator"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_creator_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Unknown field
        """
        content = [{
            "name": "Daniel Kopecký",
            "randomID": "123456"
        }]
        field = "creator"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_creator_3(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Wrong data type
        """
        content = {
            "name": "Daniel Kopecký",
        }
        field = "creator"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_creator_4(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Missing required field
        """
        content = [{
            "ORCID": "12455"
        }]
        field = "creator"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestContributor:
    def test_contributor_1(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = [{
            "name": "Daniel Kopecký",
            "ORCID": "125456",
            "scopusID": "125456",
            "researcherID": "125456",
            "czenasAutID": "125456",
            "institutionalID": "vscht123456",
            "role": [
                {
                    "links": {
                        "self": "http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/supervisor"
                    }
                }
            ]
        }]
        field = "contributor"
        base_json[field] = content
        base_json_dereferenced[field] = content
        base_json_dereferenced[field][0]["role"] = [{
            'dataCiteCode': 'Supervisor',
            'is_ancestor': False,
            'links': {
                'self':
                    'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/supervisor'
            },
            'title': {
                'cs': 'supervizor', 'en': 'supervisor'
            }
        }]
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_contributor_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Wrong datatype
        """
        content = {
            "name": "Daniel Kopecký",
            "ORCID": "125456",
            "scopusID": "125456",
            "researcherID": "125456",
            "czenasAutID": "125456",
            "institutionalID": "vscht123456",
            "role": [
                {
                    "links": {
                        "self": "http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/supervisor"
                    }
                }
            ]
        }
        field = "contributor"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_contributor_3(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Missing required field (role)
        """
        content = [{
            "name": "Daniel Kopecký",
            "ORCID": "125456",
            "scopusID": "125456",
            "researcherID": "125456",
            "czenasAutID": "125456",
            "institutionalID": "vscht123456",
        }]
        field = "contributor"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_contributor_4(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Missing required field (name)
        """
        content = {
            "role": [
                {
                    "links": {
                        "self": "http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/supervisor"
                    }
                }
            ]
        }
        field = "contributor"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestDateIssued:
    def test_date_issued_1(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020-07"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_3(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020-07-01"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_4(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        date = "2020-07-01"
        content = "bla bla %s" % date
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = date
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_5(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        date = "2020-07"
        content = "bla bla %s" % date
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = date
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_6(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020-13"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_date_issued_7(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = datetime(2020, 1, 1)
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_date_issued_8(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = ["2020-13"]
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestDateModified:
    def test_date_issued_1(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020-07"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_3(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020-07-01"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_4(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        date = "2020-07-01"
        content = "bla bla %s" % date
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = date
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_5(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        date = "2020-07"
        content = "bla bla %s" % date
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = date
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_issued_6(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "2020-13"
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_date_issued_7(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = datetime(2020, 1, 1)
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_date_issued_8(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = ["2020-13"]
        field = "dateIssued"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestResourceType:
    def test_resource_type_1(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = [
            {
                "links": {
                    "self": "http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/bakalarske-prace"
                }
            }
        ]
        field = "resourceType"
        base_json[field] = content
        # base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_resource_type_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = [
            {
                "links": {
                    "self": "http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/bla"
                }
            }
        ]
        field = "resourceType"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestExtent:
    def test_extent(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "128 s."
        field = "extent"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_extent_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Wrong data type
        """
        content = 128
        field = "extent"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestExternalLocation:
    def test_external_location(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "http://example.com"
        field = "externalLocation"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_external_location_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Wrong URL format
        """
        content = "www.example.com"
        field = "externalLocation"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestControlNumber:
    def test_control_number(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = "128"
        field = "extent"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_extent_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        """
        Wrong data type
        """
        content = 128
        field = "extent"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestWorkIdentifiers:
    def test_work_identifiers(self, app, db, taxonomy_tree, base_json, base_json_dereferenced):
        content = {
            "isbn": ["978-3-16-148410-0"],
            "issn": ["2049-3630"],
            "doi": "10.1021/acs.jced.6b00139",
            "RIV": "RIV/61388980:_____/13:00392389"
        }
        field = "workIdentifiers"
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_dereferenced
