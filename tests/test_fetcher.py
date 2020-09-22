from invenio_nusl_common.fetchers import nusl_id_fetcher
from tests.conftest import TestRecord


def test_nusl_id_fetcher(app, db):
    id_field = "control_number"
    data = {
        "title": "Test",
        id_field: "1"
    }
    record = TestRecord.create(data=data)
    fetched_id = nusl_id_fetcher(record_uuid=record.id, data=data)
    assert fetched_id.pid_type == "nusl"
    assert fetched_id.pid_value == data[id_field]
