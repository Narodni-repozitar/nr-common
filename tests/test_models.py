from nr_common.models import NRIdentifier


def test_max(app, db):
    nr_id = NRIdentifier(nr_id=1)
    db.session.add(nr_id)
    db.session.commit()
    max_ = nr_id.max()
    print(max_, type(max_))
    assert max_ == 1


def test_insert(app, db):
    nr_id = NRIdentifier()
    nr_id.insert(5)
    nr_id.insert(20)
    db.session.commit()
    last = NRIdentifier.query.order_by(NRIdentifier.nr_id.desc()).first()
    assert last.nr_id == 20
