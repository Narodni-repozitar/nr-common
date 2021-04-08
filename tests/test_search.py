import json

from flask import request
from flask_login import login_user
from flask_principal import AnonymousIdentity
from flask_security import AnonymousUser

from nr_common.search import NRRecordsSearch
from tests.helpers import set_identity


def test_search_meta(app, db, community):
    # check that cached property work
    assert NRRecordsSearch.Meta is NRRecordsSearch.Meta

    # check that Meta is correstly inherited
    assert issubclass(NRRecordsSearch.Meta, NRRecordsSearch.ActualMeta)

    # check that the owner class is set
    assert NRRecordsSearch.Meta.outer_class is NRRecordsSearch

    # get default_filter_factory
    with app.app_context():
        with app.test_request_context('/'):
            request.view_args = {'community_id': 'nr'}
            login_user(AnonymousUser())
            set_identity(AnonymousIdentity())
            q = NRRecordsSearch.Meta.default_filter_factory()

            assert q.to_dict() == {
                "bool": {
                    "must": [
                        {
                            "term": {
                                "_administration.state": "published"
                            }
                        },
                        {
                            "bool": {
                                "should": [
                                    {
                                        "term": {
                                            "_primary_community": "nr"
                                        }
                                    },
                                    {
                                        "terms": {
                                            "_communities.keyword": [
                                                "nr"
                                            ]
                                        }
                                    }
                                ],
                                "minimum_should_match": 1
                            }
                        }
                    ]
                }
            }
