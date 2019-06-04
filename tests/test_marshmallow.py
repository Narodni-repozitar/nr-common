import pytest

from invenio_nusl_common.marshmallow.json import ValueTypeSchemaV1, MultilanguageSchemaV1
from marshmallow.exceptions import ValidationError


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

    schema = ValueTypeSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == result.data


def test_valueType_load_2():
    user_data = {
        "value": "12455122"
    }

    schema = ValueTypeSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == result.data


def test_valueType_load_3():
    user_data = {
        "type": "nusl"
    }

    with pytest.raises(ValidationError):
        schema = ValueTypeSchemaV1(strict=True)
        result = schema.load(user_data)


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

    schema = MultilanguageSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == result.data


def test_multilanguage_load_2():
    user_data = {
        "name": "Text práce",
        "lang": "blbost"
    }
    with pytest.raises(ValidationError):
        schema = MultilanguageSchemaV1(strict=True)
        result = schema.load(user_data)


def test_multilanguage_load_3():
    user_data = {
        "name": "Text práce"
    }

    with pytest.raises(ValidationError):
        schema = MultilanguageSchemaV1(strict=True)
        result = schema.load(user_data)


def test_multilanguage_load_4():
    user_data = {
        "name": "Text práce",
        "lang": "CES"
    }

    final_data = {'lang': 'cze', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1(strict=True)
    result = schema.load(user_data)
    assert final_data == result.data


def test_multilanguage_load_5():
    user_data = {
        "name": "Text práce",
        "lang": "DEU"
    }

    final_data = {'lang': 'ger', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1(strict=True)
    result = schema.load(user_data)
    assert final_data == result.data


########################################################################
#                       Organization                                   #
########################################################################

# TODO: dodělat testy