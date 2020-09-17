import pytest
from marshmallow import ValidationError

from invenio_nusl_common.marshmallow import CommonMetadataSchemaV2


def test_required_fields(app, db, taxonomy_tree, base_json, base_json_derefernced):
    schema = CommonMetadataSchemaV2()
    json = base_json
    result = schema.load(json)
    assert result == base_json_derefernced


class TestAbstract:
    def test_abstract_load_1(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        abstract_ = {
            "cs": "Testovací abstrakt",
            "en": "Test abstract"
        }
        base_json["abstract"] = abstract_
        base_json_derefernced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_derefernced

    def test_abstract_load_2(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        abstract_ = [{
            "cs": "Testovací abstrakt",
            "en": "Test abstract"
        }]
        base_json["abstract"] = abstract_
        base_json_derefernced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_abstract_load_3(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        abstract_ = {
            "cs": "Testovací abstrakt",
            "pl": "Test abstract"
        }
        base_json["abstract"] = abstract_
        base_json_derefernced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_abstract_load_4(self, db, taxonomy_tree, base_json, base_json_derefernced):
        abstract_ = {
            "cze": "Testovací abstrakt",
            "en": "Test abstract"
        }
        base_json["abstract"] = abstract_
        base_json_derefernced["abstract"] = abstract_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestAccessibility:
    def test_accessibility(self, db, taxonomy_tree, base_json, base_json_derefernced):
        acc_ = {
            "cs": "Dostupné kdesi blabla",
            "en": "Avallable at blabla"
        }
        base_json["accessibility"] = acc_
        base_json_derefernced["accessibility"] = acc_
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_derefernced

    def test_accessibility_2(self, db, taxonomy_tree, base_json, base_json_derefernced):
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
        base_json_derefernced["accessibility"] = acc_
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestAccessRights:
    def test_access_rights_1(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        ar = {
        }
        base_json["accessRights"] = ar
        base_json_derefernced["accessRights"] = ar
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_access_rights_2(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        ar = [{
        }]
        base_json["accessRights"] = ar
        base_json_derefernced["accessRights"] = ar
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_access_rights_3(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        ar = [{
            "links": {
                "self": "bla"
            }
        }]
        base_json["accessRights"] = ar
        base_json_derefernced["accessRights"] = ar
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValueError):
            schema.load(base_json)


class TestCreator:
    def test_creator(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
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
        base_json_derefernced[field] = content
        schema = CommonMetadataSchemaV2()
        result = schema.load(base_json)
        assert result == base_json_derefernced

    def test_creator_2(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        """
        Unknown field
        """
        content = [{
            "name": "Daniel Kopecký",
            "randomID": "123456"
        }]
        field = "creator"
        base_json[field] = content
        base_json_derefernced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_creator_3(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        """
        Wrong data type
        """
        content = {
            "name": "Daniel Kopecký",
        }
        field = "creator"
        base_json[field] = content
        base_json_derefernced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_creator_4(self, app, db, taxonomy_tree, base_json, base_json_derefernced):
        """
        Missing required field
        """
        content = [{
            "ORCID": "12455"
        }]
        field = "creator"
        base_json[field] = content
        base_json_derefernced[field] = content
        schema = CommonMetadataSchemaV2()
        with pytest.raises(ValidationError):
            schema.load(base_json)
