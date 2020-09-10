import pytest
from marshmallow import Schema, ValidationError

from invenio_nusl_common.marshmallow.fields import NRDate, ISBN, ISSN


# NRDate tests
@pytest.mark.parametrize("test_input,expected",
                         [("2019-12-31", "2019-12-31"), ("2019-12", "2019-12"), ("2019", "2019"),
                          ("2018-12-31 / 2019-12-31", "2018-12-31 / 2019-12-31"),
                          ("2018-12 / 2019-12", "2018-12 / 2019-12"),
                          ("p2019", "2019"), ("c2019", "2019"), ("cop2019", "2019"),
                          ("[2019]", "2019"), ("©2019", "2019"), ("℗2019", "2019"),
                          ("2018-2019", "2018 / 2019"), ("copyright2019", "2019"),
                          ("fonogram2019", "2019"), ("2018 - 2019", "2018 / 2019")
                          ])
def test_NRDate(test_input, expected):
    class TestSchema(Schema):
        date = NRDate(required=True)

    data = {
        "date": test_input
    }
    schema = TestSchema()
    res = schema.load(data)
    assert res["date"] == expected


def test_NRDate_2():
    class TestSchema(Schema):
        date = NRDate(required=True)

    data = {
        "date": "2019 2018 2020"
    }
    schema = TestSchema()
    with pytest.raises(ValidationError):
        res = schema.load(data)


def test_NRDate_3():
    class TestSchema(Schema):
        date = NRDate(required=True)

    data = {
        "date": "2021-07-08"
    }
    schema = TestSchema()
    with pytest.raises(ValidationError):
        res = schema.load(data)


# ISBN
@pytest.mark.parametrize("test_input,expected",
                         [
                             ("978-1-56619-909-4", "978-1-56619-909-4"),
                             ("9781566199094", "978-1-56619-909-4"),
                             ("1-56619-909-3", "1-56619-909-3"),
                             ("1566199093", "1-56619-909-3"),
                         ])
def test_ISBN(test_input, expected):
    class TestSchema(Schema):
        isbn = ISBN(required=True)

    data = {
        "isbn": test_input
    }
    schema = TestSchema()
    res = schema.load(data)
    assert res["isbn"] == expected


def test_ISBN_2():
    class TestSchema(Schema):
        isbn = ISBN(required=True)

    data = {
        "isbn": "978-1-56619-909-7"  # wrong control sum
    }
    schema = TestSchema()
    with pytest.raises(ValidationError):
        schema.load(data)


def test_ISBN_3():
    class TestSchema(Schema):
        isbn = ISBN(required=True)

    data = {
        "isbn": "978-1-56619-909-4 a 1-56619-909-3"
    }
    schema = TestSchema()
    with pytest.raises(ValidationError):
        schema.load(data)


# ISSN
@pytest.mark.parametrize("test_input,expected",
                         [
                             ("2049-3630", "2049-3630"),
                             ("20493630", "2049-3630"),
                         ])
def test_ISSN(test_input, expected):
    class TestSchema(Schema):
        issn = ISSN(required=True)

    data = {
        "issn": test_input
    }
    schema = TestSchema()
    res = schema.load(data)
    assert res["issn"] == expected


def test_ISSN_2():
    class TestSchema(Schema):
        issn = ISSN(required=True)

    data = {
        "issn": "2049-3631"
    }
    schema = TestSchema()
    with pytest.raises(ValidationError):
        schema.load(data)

def test_ISSN_3():
    class TestSchema(Schema):
        issn = ISSN(required=True)

    data = {
        "issn": "2049-36311"
    }
    schema = TestSchema()
    with pytest.raises(ValidationError):
        schema.load(data)

def test_ISSN_4():
    class TestSchema(Schema):
        issn = ISSN(required=True)

    data = {
        "issn": "2049a3631"
    }
    schema = TestSchema()
    with pytest.raises(ValidationError):
        schema.load(data)
