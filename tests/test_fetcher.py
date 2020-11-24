from nr_common.fetchers import nr_id_fetcher
from tests.conftest import TestRecord


def test_nr_id_fetcher(app, db):
    id_field = "control_number"
    data = {
        "title": "Test",
        id_field: "1"
    }
    record = TestRecord.create(data=data)
    fetched_id = nr_id_fetcher(record_uuid=record.id, data=data)
    assert fetched_id.pid_type == "nrcom"
    assert fetched_id.pid_value == data[id_field]
