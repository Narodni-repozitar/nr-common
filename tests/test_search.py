import functools

from flask import request
from flask.views import View
from flask_login import login_user
from flask_principal import AnonymousIdentity
from flask_security import AnonymousUser
from invenio_records_rest.query import default_search_factory
from oarepo_search.query_parsers import query_parser

from nr_common.search import NRRecordsSearch, community_search_factory
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


def test_search_class(app, client):
    def my_search_factory(*args, **kwargs):
        my_query_parser = functools.partial(query_parser, index_name="test-index",
                                            endpoint_name="test-endpoint")

        return default_search_factory(*args,
                                      query_parser=my_query_parser, **kwargs)

    view = View()
    with app.test_request_context(
            '/path/2017?q=bla'):
        # request.__setattr__("view_args", {"community_id": 1})
        # setattr(request, "endpoint", "invenio_records_rest.draft-nresults-community_list")
        search_obj = NRRecordsSearch()
        search = search_obj.with_preference_param().params(version=True)
        setattr(search, '_original_index', ['test_index'])
        search, qs_kwargs = my_search_factory(view, search)
    assert search.to_dict() == {
        'query': {
            'bool': {
                'minimum_should_match': '0<1',
                'filter': [{'term': {'_administration.state': 'published'}}],
                'must': [{'query_string': {'query': 'bla'}}]
            }
        }, '_source': []
    }
