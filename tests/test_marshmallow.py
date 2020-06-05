import pytest
from marshmallow.exceptions import ValidationError

from invenio_nusl_common.marshmallow.json import ValueTypeSchemaV1, MultilanguageSchemaV1, \
    OrganizationSchemaV1


########################################################################
#                           ValueType                                  #
########################################################################

def test_valueType_dump_1():
    json = {
        "value": "151515",
        "type": "nusl"
    }
    valueType = ValueTypeSchemaV1()
    assert json == valueType.dump(json).data


def test_valueType_dump_2():
    json = {
        "value": "151515",
        "type": "nusl",
        "pole": "blbost"
    }
    valueType = ValueTypeSchemaV1()
    assert json != valueType.dump(json).data


def test_valueType_dump_3():
    json = {
        "value": "151515",
        "pole": "blbost"
    }
    valueType = ValueTypeSchemaV1()
    assert json != valueType.dump(json).data


def test_valueType_load_1():
    user_data = {
        "value": "12455122",
        "type": "nusl"
    }

    schema = ValueTypeSchemaV1()
    result = schema.load(user_data)
    assert user_data == result.data


def test_valueType_load_2():
    user_data = {
        "value": "12455122"
    }

    with pytest.raises(ValidationError):
        schema = ValueTypeSchemaV1()
        schema.load(user_data)


def test_valueType_load_3():
    user_data = {
        "type": "nusl"
    }

    with pytest.raises(ValidationError):
        schema = ValueTypeSchemaV1()
        result = schema.load(user_data)


def test_valueType_load_4():
    user_data = {
        "value": None,
        "type": None
    }

    schema = ValueTypeSchemaV1()
    result = schema.load(user_data)
    assert user_data == result.data


########################################################################
#                       Multilanguage                                  #
########################################################################

def test_multiLanguage_dump_1():
    json = {
        "name": "Název práce",
        "lang": "CZE"
    }
    multiLanguage = MultilanguageSchemaV1()
    assert json == multiLanguage.dump(json).data


def test_multiLanguage_dump_2():
    json = {
        "name": "Název práce",
        "lang": "CZE",
        "pole": "blbost"
    }
    multiLanguage = MultilanguageSchemaV1()
    assert json != multiLanguage.dump(json).data


def test_multiLanguage_dump_3():
    json = {
        "name": "Název práce",
        "pole": "blbost"
    }
    multiLanguage = MultilanguageSchemaV1()
    assert json != multiLanguage.dump(json).data


def test_multiLanguage_dump_4():
    json = {
        "name": "Název práce"
    }
    multiLanguage = MultilanguageSchemaV1()
    assert json == multiLanguage.dump(json).data


def test_multilanguage_load_1():
    user_data = {
        "name": "Text práce",
        "lang": "CZE"
    }

    schema = MultilanguageSchemaV1()
    result = schema.load(user_data)
    assert user_data == result.data


def test_multilanguage_load_2():
    user_data = {
        "name": "Text práce",
        "lang": "blbost"
    }
    with pytest.raises(ValidationError):
        schema = MultilanguageSchemaV1()
        result = schema.load(user_data)


def test_multilanguage_load_3():
    user_data = {
        "name": "Text práce"
    }

    with pytest.raises(ValidationError):
        schema = MultilanguageSchemaV1()
        result = schema.load(user_data)


def test_multilanguage_load_4():
    user_data = {
        "name": "Text práce",
        "lang": "CES"
    }

    final_data = {'lang': 'cze', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1()
    result = schema.load(user_data)
    assert final_data == result.data


def test_multilanguage_load_5():
    user_data = {
        "name": "Text práce",
        "lang": "DEU"
    }

    final_data = {'lang': 'ger', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1()
    result = schema.load(user_data)
    assert final_data == result.data


def test_multilanguage_load_6():
    user_data = {
        "name": "Text práce",
        "lang": "cs"
    }

    final_data = {'lang': 'cze', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1()
    result = schema.load(user_data)
    assert final_data == result.data


def test_multilanguage_load_7():
    user_data = {
        "name": "Text práce",
        "lang": "en"
    }

    final_data = {'lang': 'eng', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1()
    result = schema.load(user_data)
    assert final_data == result.data


########################################################################
#                       Organization                                   #
########################################################################
def test_organization_dump_1():
    user_data = {
        "id": {
            "value": "60461373",
            "type": "IČO"
        },
        "address": "Technická 1905/5, Dejvice, 160 00 Praha",
        "contactPoint": "info@vscht.cz",
        "name": {
            "name": "Vysoká škola chemicko-technologická",
            "lang": "cze"
        },
        "url": "https://www.vscht.cz/",
        "provider": True,
        "isPartOf": ["public_uni", "edu"]  # TODO: Dodělat kontrolovaný slovník organizací
    }
    schema = OrganizationSchemaV1()
    result = schema.load(user_data)
    assert user_data == result.data


def test_organization_load_1():
    user_data = {
        "id": {
            "value": "60461373",
            "type": "IČO"
        },
        "address": "Technická 1905/5, Dejvice, 160 00 Praha",
        "contactPoint": "info@vscht.cz",
        "name": {
            "name": "Vysoká škola chemicko-technologická",
            "lang": "cze"
        },
        "url": "https://www.vscht.cz/",
        "provider": True,
        "isPartOf": ["public_uni", "edu"]  # TODO: Dodělat kontrolovaný slovník organizací
    }

    schema = OrganizationSchemaV1()
    result = schema.load(user_data)
    assert user_data == result.data


def test_organization_load_2():
    user_data = {
        "id": {
            "value": "60461373",
            "type": "IČO"
        },
        "address": "Technická 1905/5, Dejvice, 160 00 Praha",
        "contactPoint": "info@vscht.cz",
        "name": {
            "name": "Vysoká škola chemicko-technologická",
            "lang": "cz"
        },
        "url": "https://www.vscht.cz/",
        "provider": True,
        "isPartOf": ["public_uni", "edu"]  # TODO: Dodělat kontrolovaný slovník organizací
    }

    with pytest.raises(ValidationError):
        schema = OrganizationSchemaV1()
        schema.load(user_data)
