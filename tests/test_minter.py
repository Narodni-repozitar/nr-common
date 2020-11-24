from invenio_pidstore.models import PersistentIdentifier

from nr_common.minters import nr_id_minter
from tests.conftest import TestRecord


def test_nr_id_minter(app, db):
    data = {
        "title": "Test",
    }
    record = TestRecord.create(data=data)
    minted_id = nr_id_minter(record_uuid=record.id, data=data)
    assert data["control_number"] == "1"


def test_nr_id_minter_2(app, db):
    data = {
        "title": "Test",
        "control_number": "68"
    }
    record = TestRecord.create(data=data)
    minted_id = nr_id_minter(record_uuid=record.id, data=data)
    db.session.commit()
    PID = PersistentIdentifier.get(pid_type=minted_id.pid_type, pid_value=minted_id.pid_value)
    assert PID.pid_value == "68"
    assert PID.pid_type == "nrcom"
    assert data["control_number"] == "68"
