import re

import arrow
import idutils
import isbnlib
from arrow import ParserError
from marshmallow import fields, ValidationError
from stdnum import issn
from stdnum.exceptions import InvalidChecksum, InvalidLength, InvalidFormat, InvalidComponent


class NRDate(fields.Field):
    """Field that parse date and date range.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        return serialize_date(value)


class Year(fields.Field):

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            value = str(value).strip()
            a = arrow.get(value)
            if a < arrow.get("1700"):
                raise ValidationError(
                    "Date is lower then 1700")
            if a > arrow.get():
                raise ValidationError("Cannot use year higher than current year")
            return a.format("YYYY")
        except ParserError:
            raise ValidationError("Wrong date format")


class ISBN(fields.Field):

    def _deserialize(self, value, attr, data, **kwargs):
        return self.extract_isbn(value)

    @staticmethod
    def extract_isbn(value):
        isbns = isbnlib.get_isbnlike(value)
        isbn = isbns[0]
        if len(isbns) > 1:
            raise ValidationError("Too much ISBN numbers")
        elif (len(isbns) == 0) or (not isbnlib.is_isbn10(isbn) and not isbnlib.to_isbn13(isbn)):
            raise ValidationError("It is not ISBN number")
        elif len(isbns) == 1:
            return isbnlib.mask(isbn)
        else:
            raise ValidationError("Unexpected option")


class ISSN(fields.Field):

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            issn.validate(value)
            return issn.format(value)
        except (InvalidChecksum, InvalidLength, InvalidFormat, InvalidComponent) as e:
            raise ValidationError(str(e))


class DOI(fields.Field):

    def _deserialize(self, value, attr, data, **kwargs):
        doi = idutils.is_doi(value)
        if not doi:
            raise ValidationError(f"It is not valid doi: \"{value}\"")
        return doi.string


class RIV(fields.Field):

    def _deserialize(self, value, attr, data, **kwargs):
        pattern = r"RIV/\w{8}:\w{5}/\d{2}:\d{8}$"
        match = re.match(pattern, value.strip())
        if not match:
            raise ValidationError(f"It is not valid RIV id: \"{value.strip()}\"")
        return match.string


def extract_date(value):
    try:
        obj = re.search(r"(\d{4})[/.-]+(\d{4})", value)
    except TypeError as e:
        raise ValidationError(str(e))
    if obj:
        groups = obj.groups()
        return [(groups[0],), (groups[1],)]
    pattern = r"(\d{4})[/.-]?(\d{2})?[/.-]?(\d{2})?"
    dates = re.findall(pattern, value)
    if dates:
        return dates
    return


def serialize_date(value):
    dates = extract_date(value)
    dates = _serialize_dates(dates)
    if len(dates) > 2:
        raise ValidationError("Too much dates. Only two dates are allowed for date range")
    elif len(dates) == 2:
        return " / ".join(dates)
    elif len(dates) == 1:
        return dates[0]
    else:
        raise ValidationError(f"Unsupported date format or missing date in value: \"{value}\"")


def _serialize_dates(dates):
    result = []
    for date in dates:
        new_date = [stage.strip() for stage in date if len(stage) > 0]
        l = len(new_date)
        date_str = "-".join(new_date)
        try:
            a = arrow.get(date_str)
        except ValueError as e:
            raise ValidationError(str(e))
        if a > arrow.get():
            raise ValidationError("Can't select a future date")
        if l == 3:
            result.append(a.format("YYYY-MM-DD"))
        elif l == 2:
            result.append(a.format("YYYY-MM"))
        elif l == 1:
            result.append(a.format("YYYY"))
        else:
            raise ValidationError("Wrong date format")
    return result


class OAI(fields.Field):

    def _deserialize(self, value, attr, data, **kwargs):
        pattern = r"oai:[a-zA-Z][a-zA-Z0-9\-]*(\.[a-zA-Z][a-zA-Z0-9\-]*)+:[a-zA-Z0-9\-_\.!~\*'\(\);/\?:@&=\+$,%]+"
        match = re.match(pattern, value.strip())
        if not match:
            raise ValidationError(f"It is not valid oai identifier \"{value}\"")
        return match.string
