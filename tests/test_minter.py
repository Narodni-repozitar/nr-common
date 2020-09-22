from invenio_nusl_common.minters import nusl_id_minter
from tests.conftest import TestRecord


def test_nusl_id_fetcher(app, db):
    data = {
        "title": "Test",
    }
    record = TestRecord.create(data=data)
    minted_id = nusl_id_minter(record_uuid=record.id, data=data)
    assert data["control_number"] == "1"
