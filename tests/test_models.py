from invenio_nusl_common.models import NuslIdentifier


def test_max(app, db):
    nusl_id = NuslIdentifier(nusl_id=1)
    db.session.add(nusl_id)
    db.session.commit()
    max_ = nusl_id.max()
    print(max_, type(max_))
    assert max_ == 1


def test_insert(app, db):
    nusl_id = NuslIdentifier()
    nusl_id.insert(5)
    nusl_id.insert(20)
    db.session.commit()
    last = NuslIdentifier.query.order_by(NuslIdentifier.nusl_id.desc()).first()
    assert last.nusl_id == 20
