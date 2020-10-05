from nr_common.minters import nr_id_minter
from tests.conftest import TestRecord


def test_nr_id_fetcher(app, db):
    data = {
        "title": "Test",
    }
    record = TestRecord.create(data=data)
    minted_id = nr_id_minter(record_uuid=record.id, data=data)
    assert data["control_number"] == "1"
