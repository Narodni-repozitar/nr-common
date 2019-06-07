import pytest

from invenio_nusl_common.marshmallow.json import ValueTypeSchemaV1, MultilanguageSchemaV1, NUSLDoctypeSchemaV1, \
    RIVDoctypeSchemaV1
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

    with pytest.raises(ValidationError):
        schema = ValueTypeSchemaV1(strict=True)
        schema.load(user_data)


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


def test_multilanguage_load_6():
    user_data = {
        "name": "Text práce",
        "lang": "cs"
    }

    final_data = {'lang': 'cze', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1(strict=True)
    result = schema.load(user_data)
    assert final_data == result.data


def test_multilanguage_load_7():
    user_data = {
        "name": "Text práce",
        "lang": "en"
    }

    final_data = {'lang': 'eng', 'name': 'Text práce'}

    schema = MultilanguageSchemaV1(strict=True)
    result = schema.load(user_data)
    assert final_data == result.data


########################################################################
#                       DocTypeNUSL                                    #
########################################################################
def test_doctype_dump_1():
    json = {
        "term": "studie",
        "bterm": "anl_met_mat"
    }
    multiLanguage = NUSLDoctypeSchemaV1(strict=True)
    assert json == multiLanguage.dump(json).data


def test_doctype_load_1():
    user_data = {
        "term": "studie",
        "bterm": "anl_met_mat"
    }

    schema = NUSLDoctypeSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == result.data


def test_doctype_load_2():
    user_data = {
        "term": "neexistuje",
        "bterm": "anl_met_mat"
    }

    with pytest.raises(ValidationError):
        schema = NUSLDoctypeSchemaV1(strict=True)
        schema.load(user_data)


def test_doctype_load_3():
    user_data = {
        "bterm": "anl_met_mat"
    }

    with pytest.raises(ValidationError):
        schema = NUSLDoctypeSchemaV1(strict=True)
        schema.load(user_data)


def test_doctype_load_4():
    user_data = {
        "bterm": "neexistuje"
    }

    with pytest.raises(ValidationError):
        schema = NUSLDoctypeSchemaV1(strict=True)
        schema.load(user_data)


def test_doctype_load_5():
    user_data = {
        "term": "letaky",
        "bterm": "vskp"
    }

    with pytest.raises(ValidationError):
        schema = NUSLDoctypeSchemaV1(strict=True)
        schema.load(user_data)


########################################################################
#                       DocTypeRIV                                    #
########################################################################
def test_doctype_RIV_dump_1():
    json = {
        "term": "polop",
        "bterm": "Z"
    }
    multiLanguage = RIVDoctypeSchemaV1(strict=True)
    assert json == multiLanguage.dump(json).data


def test_doctype_RIV_load_1():
    user_data = {
        "term": "polop",
        "bterm": "Z"
    }

    schema = RIVDoctypeSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == result.data


def test_doctype_RIV_load_2():
    user_data = {
        "term": "neexistuje",
        "bterm": "Z"
    }

    with pytest.raises(ValidationError):
        schema = RIVDoctypeSchemaV1(strict=True)
        schema.load(user_data)


def test_doctype_RIV_load_3():
    user_data = {
        "bterm": "Z"
    }

    schema = RIVDoctypeSchemaV1(strict=True)
    result = schema.load(user_data)
    assert user_data == result.data


def test_doctype_RIV_load_4():
    user_data = {
        "bterm": "Z",
        "term": None
    }
    with pytest.raises(ValidationError):
        schema = RIVDoctypeSchemaV1(strict=True)
        schema.load(user_data)

def test_doctype_RIV_load_5():
    user_data = {
        "bterm": "P",
        "term": None
    }
    with pytest.raises(ValidationError):
        schema = RIVDoctypeSchemaV1(strict=True)
        schema.load(user_data)


########################################################################
#                       Organization                                   #
########################################################################

# TODO: dodělat testy
