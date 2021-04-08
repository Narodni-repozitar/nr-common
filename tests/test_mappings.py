import json
import uuid
from pprint import pprint


def test_mapping_1(app, es, es_index, base_json_dereferenced):
    mappings = app.extensions["invenio-search"].mappings
    mapping_path = mappings["nr_common-nr-common-v1.0.0"]
    with open(mapping_path, "r") as f:
        body = json.load(f)
    index_name = "test_index"
    es.indices.put_mapping(body=body["mappings"], index=index_name)
    uuid_ = uuid.uuid4()
    response = es.index(
        index=index_name,
        body=base_json_dereferenced,
        id=uuid_
    )
    print("\n", "RESPONSE", "\n", response)
    es_record = es.get(index_name, id=uuid_)
    print("\n" * 5)
    pprint(es_record["_source"])
    assert es_record["_source"] == base_json_dereferenced
    assert body == {
        'aliases': {'{PREFIX}nr-all': {}},
        'mappings': {
            'date_detection': False,
            'dynamic': False,
            'numeric_detection': False,
            'properties': {
                '$schema': {'index': True, 'type': 'keyword'},
                '_administration': {
                    'properties': {
                        'communities': {'type': 'keyword'},
                        'owned_by': {'type': 'integer'},
                        'primaryCommunity': {'type': 'keyword'},
                        'state': {'type': 'keyword'}
                    },
                    'type': 'object'},
                'abstract': {
                    'properties': {
                        'bg': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'cs': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'da': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'de': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'el': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'es': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'fr': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'hu': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'it': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'lt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'nl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'no': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ro': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ru': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sk': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sv': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'object'
                },
                'accessRights': {
                    'properties': {
                        'is_ancestor': {'type': 'boolean'},
                        'level': {'type': 'integer'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'relatedURI': {
                            'properties': {
                                'coar': {'type': 'keyword'},
                                'eprint': {'type': 'keyword'},
                                'vocabs': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'title': {
                            'properties': {
                                'bg': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        }
                    },
                    'type': 'object'
                },
                'accessibility': {
                    'properties': {
                        'bg': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'cs': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'da': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'de': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'el': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'es': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'fr': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'hu': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'it': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'lt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'nl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'no': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ro': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ru': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sk': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sv': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'object'
                },
                'contributor': {
                    'properties': {
                        'ORCID': {'type': 'keyword'},
                        'czenasAutID': {'type': 'keyword'},
                        'institutionalID': {'type': 'keyword'},
                        'name': {
                            'copy_to': 'person',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'researcherID': {'type': 'keyword'},
                        'role': {
                            'properties': {
                                'dataCiteCode': {'type': 'keyword'},
                                'is_ancestor': {'type': 'boolean'},
                                'level': {'type': 'integer'},
                                'links': {
                                    'properties': {
                                        'parent': {'type': 'keyword'},
                                        'self': {'type': 'keyword'}
                                    },
                                    'type': 'object'
                                },
                                'marcCode': {'type': 'keyword'},
                                'title': {
                                    'properties': {
                                        'bg': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'cs': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'da': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'de': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'el': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'en': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'es': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'fr': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'hu': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'it': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'lt': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'nl': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'no': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'pl': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'pt': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'ro': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'ru': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'sk': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'sv': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        }
                                    },
                                    'type': 'object'
                                }
                            },
                            'type': 'object'
                        },
                        'scopusID': {'type': 'keyword'},
                        'vedidk': {'type': 'keyword'}
                    },
                    'type': 'nested'
                },
                'control_number': {'type': 'keyword'},
                'creator': {
                    'properties': {
                        'ORCID': {'type': 'keyword'},
                        'czenasAutID': {'type': 'keyword'},
                        'institutionalID': {'type': 'keyword'},
                        'name': {
                            'copy_to': 'person',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'researcherID': {'type': 'keyword'},
                        'scopusID': {'type': 'keyword'},
                        'vedidk': {'type': 'keyword'}
                    },
                    'type': 'nested'
                },
                'dateAll': {
                    'fields': {
                        'date': {
                            'format': 'yyyy-MM-dd||yyyy-MM||yyyy',
                            'ignore_malformed': True,
                            'type': 'date'
                        }
                    },
                    'type': 'keyword'
                },
                'dateIssued': {
                    'copy_to': 'dateAll',
                    'fields': {
                        'date': {
                            'format': 'yyyy-MM-dd||yyyy-MM||yyyy',
                            'ignore_malformed': True,
                            'type': 'date'
                        }
                    },
                    'type': 'keyword'
                },
                'dateModified': {
                    'copy_to': 'dateAll',
                    'fields': {
                        'date': {
                            'format': 'yyyy-MM-dd||yyyy-MM||yyyy',
                            'ignore_malformed': True,
                            'type': 'date'
                        }
                    },
                    'type': 'keyword'
                },
                'entities': {
                    'properties': {
                        'aliases': {
                            'fields': {
                                'keyword': {
                                    'ignore_above': 256,
                                    'type': 'keyword'
                                }
                            },
                            'type': 'text'
                        },
                        'formerNames': {
                            'fields': {
                                'keyword': {
                                    'ignore_above': 256,
                                    'type': 'keyword'
                                }
                            },
                            'type': 'text'
                        },
                        'ico': {'type': 'keyword'},
                        'is_ancestor': {'type': 'boolean'},
                        'level': {'type': 'integer'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'provider': {'type': 'boolean'},
                        'relatedID': {
                            'properties': {
                                'type': {
                                    'fields': {
                                        'keyword': {
                                            'ignore_above': 256,
                                            'type': 'keyword'
                                        }
                                    },
                                    'type': 'text'
                                },
                                'value': {
                                    'fields': {
                                        'keyword': {
                                            'ignore_above': 1000,
                                            'type': 'keyword'
                                        }
                                    },
                                    'type': 'text'
                                }
                            }
                        },
                        'title': {
                            'properties': {
                                'bg': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        },
                        'url': {'type': 'keyword'}
                    },
                    'type': 'object'
                },
                'extent': {'index': False, 'type': 'keyword'},
                'externalLocation': {'type': 'keyword'},
                'fundingReference': {
                    'properties': {
                        'funder': {
                            'properties': {
                                'aliases': {
                                    'fields': {
                                        'keyword': {
                                            'ignore_above': 256,
                                            'type': 'keyword'
                                        }
                                    },
                                    'type': 'text'
                                },
                                'formerNames': {
                                    'fields': {
                                        'keyword': {
                                            'ignore_above': 256,
                                            'type': 'keyword'
                                        }
                                    },
                                    'type': 'text'
                                },
                                'ico': {'type': 'keyword'},
                                'is_ancestor': {'type': 'boolean'},
                                'level': {'type': 'integer'},
                                'links': {
                                    'properties': {
                                        'parent': {'type': 'keyword'},
                                        'self': {'type': 'keyword'}
                                    },
                                    'type': 'object'
                                },
                                'provider': {'type': 'boolean'},
                                'relatedID': {
                                    'properties': {
                                        'type': {
                                            'fields': {
                                                'keyword': {
                                                    'ignore_above': 256,
                                                    'type': 'keyword'
                                                }
                                            },
                                            'type': 'text'
                                        },
                                        'value': {
                                            'fields': {
                                                'keyword': {
                                                    'ignore_above': 1000,
                                                    'type': 'keyword'
                                                }
                                            },
                                            'type': 'text'
                                        }
                                    }
                                },
                                'title': {
                                    'properties': {
                                        'bg': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'cs': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'da': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'de': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'el': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'en': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'es': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'fr': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'hu': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'it': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'lt': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'nl': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'no': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'pl': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'pt': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'ro': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'ru': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'sk': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'sv': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        }
                                    },
                                    'type': 'object'
                                },
                                'url': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'fundingProgram': {
                            'fields': {'keyword': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'projectID': {'type': 'keyword'},
                        'projectName': {
                            'fields': {'keyword': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'nested'
                },
                'isGL': {'type': 'boolean'},
                'keywords': {
                    'properties': {
                        'bg': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'cs': {
                            'copy_to': 'subjectKeyword',
                            'type': 'keyword'
                        },
                        'da': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'de': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'el': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
                            'copy_to': 'subjectKeyword',
                            'type': 'keyword'
                        },
                        'es': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'fr': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'hu': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'it': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'lt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'nl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'no': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ro': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ru': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sk': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sv': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'object'
                },
                'language': {
                    'properties': {
                        'is_ancestor': {'type': 'boolean'},
                        'level': {'type': 'integer'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'title': {
                            'properties': {
                                'bg': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        }
                    },
                    'type': 'object'
                },
                'note': {'type': 'text'},
                'person': {
                    'fields': {'keyword': {'type': 'keyword'}},
                    'type': 'text'
                },
                'provider': {
                    'properties': {
                        'aliases': {
                            'fields': {
                                'keyword': {
                                    'ignore_above': 256,
                                    'type': 'keyword'
                                }
                            },
                            'type': 'text'
                        },
                        'formerNames': {
                            'fields': {
                                'keyword': {
                                    'ignore_above': 256,
                                    'type': 'keyword'
                                }
                            },
                            'type': 'text'
                        },
                        'ico': {'type': 'keyword'},
                        'is_ancestor': {'type': 'boolean'},
                        'level': {'type': 'integer'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'provider': {'type': 'boolean'},
                        'relatedID': {
                            'properties': {
                                'type': {
                                    'fields': {
                                        'keyword': {
                                            'ignore_above': 256,
                                            'type': 'keyword'
                                        }
                                    },
                                    'type': 'text'
                                },
                                'value': {
                                    'fields': {
                                        'keyword': {
                                            'ignore_above': 1000,
                                            'type': 'keyword'
                                        }
                                    },
                                    'type': 'text'
                                }
                            }
                        },
                        'title': {
                            'properties': {
                                'bg': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        },
                        'url': {'type': 'keyword'}
                    },
                    'type': 'object'
                },
                'publicationPlace': {
                    'properties': {
                        'country': {
                            'properties': {
                                'is_ancestor': {'type': 'boolean'},
                                'level': {'type': 'integer'},
                                'links': {
                                    'properties': {
                                        'parent': {'type': 'keyword'},
                                        'self': {'type': 'keyword'}
                                    },
                                    'type': 'object'
                                },
                                'title': {
                                    'properties': {
                                        'bg': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'cs': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'da': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'de': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'el': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'en': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'es': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'fr': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'hu': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'it': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'lt': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'nl': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'no': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'pl': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'pt': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'ro': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'ru': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'sk': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'sv': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        }
                                    },
                                    'type': 'object'
                                }
                            },
                            'type': 'object'
                        },
                        'place': {
                            'fields': {'keyword': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'nested'
                },
                'publisher': {
                    'fields': {'keyword': {'type': 'keyword'}},
                    'type': 'text'
                },
                'recordIdentifiers': {
                    'properties': {
                        'catalogueSysNo': {'type': 'keyword'},
                        'nrcrHandle': {'type': 'keyword'},
                        'nrcrOAI': {'type': 'keyword'},
                        'nuslOAI': {'type': 'keyword'},
                        'originalRecord': {'type': 'keyword'},
                        'originalRecordOAI': {'type': 'keyword'}
                    },
                    'type': 'object'
                },
                'relatedItem': {
                    'properties': {
                        'itemDOI': {'type': 'keyword'},
                        'itemEndPage': {'type': 'keyword'},
                        'itemISBN': {'type': 'keyword'},
                        'itemISSN': {'type': 'keyword'},
                        'itemIssue': {'type': 'keyword'},
                        'itemRelationType': {
                            'properties': {
                                'is_ancestor': {'type': 'boolean'},
                                'level': {'type': 'integer'},
                                'links': {
                                    'properties': {
                                        'parent': {'type': 'keyword'},
                                        'self': {'type': 'keyword'}
                                    },
                                    'type': 'object'
                                }
                            },
                            'type': 'object'
                        },
                        'itemStartPage': {'type': 'keyword'},
                        'itemTitle': {
                            'fields': {'keyword': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'itemURL': {'type': 'keyword'},
                        'itemVolume': {'type': 'keyword'},
                        'itemYear': {'type': 'keyword'}
                    },
                    'type': 'nested'
                },
                'resourceType': {
                    'properties': {
                        'is_ancestor': {'type': 'boolean'},
                        'level': {'type': 'integer'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'title': {
                            'properties': {
                                'bg': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        }
                    },
                    'type': 'object'
                },
                'rights': {
                    'properties': {
                        'icon': {'type': 'keyword'},
                        'is_ancestor': {'type': 'boolean'},
                        'level': {'type': 'integer'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'related_URI': {'type': 'keyword'},
                        'title': {
                            'properties': {
                                'bg': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        }
                    },
                    'type': 'object'
                },
                'rulesExceptions': {
                    'properties': {
                        'element': {'type': 'text'},
                        'exception': {'type': 'keyword'},
                        'path': {'type': 'keyword'},
                        'phase': {'type': 'keyword'}
                    },
                    'type': 'nested'
                },
                'series': {
                    'properties': {
                        'seriesTitle': {
                            'fields': {'keyword': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'seriesVolume': {'type': 'keyword'}
                    },
                    'type': 'nested'
                },
                'subject': {
                    'properties': {
                        'DateCreated': {'type': 'date'},
                        'DateEstablished': {'type': 'date'},
                        'DateRevised': {'type': 'date'},
                        'TreeNumberList': {
                            'fields': {
                                'keyword': {
                                    'ignore_above': 256,
                                    'type': 'keyword'
                                }
                            },
                            'type': 'text'
                        },
                        'altLabel': {
                            'properties': {
                                'bg': {
                                    'copy_to': 'subjectAll.bg',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'copy_to': 'subjectAll.cs',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'copy_to': 'subjectAll.da',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'copy_to': 'subjectAll.de',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'copy_to': 'subjectAll.el',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'copy_to': 'subjectAll.en',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'copy_to': 'subjectAll.es',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'copy_to': 'subjectAll.fr',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'copy_to': 'subjectAll.hu',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'copy_to': 'subjectAll.it',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'copy_to': 'subjectAll.lt',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'copy_to': 'subjectAll.nl',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'copy_to': 'subjectAll.no',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'copy_to': 'subjectAll.pl',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'copy_to': 'subjectAll.pt',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'copy_to': 'subjectAll.ro',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'copy_to': 'subjectAll.ru',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'copy_to': 'subjectAll.sk',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'copy_to': 'subjectAll.sv',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        },
                        'is_ancestor': {'type': 'boolean'},
                        'level': {'type': 'integer'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'relatedURI': {'type': 'keyword'},
                        'title': {
                            'properties': {
                                'bg': {
                                    'copy_to': 'subjectAll.bg',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'cs': {
                                    'copy_to': 'subjectAll.cs',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'da': {
                                    'copy_to': 'subjectAll.da',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'de': {
                                    'copy_to': 'subjectAll.de',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'el': {
                                    'copy_to': 'subjectAll.el',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'copy_to': 'subjectAll.en',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'es': {
                                    'copy_to': 'subjectAll.es',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'fr': {
                                    'copy_to': 'subjectAll.fr',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'hu': {
                                    'copy_to': 'subjectAll.hu',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'it': {
                                    'copy_to': 'subjectAll.it',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'lt': {
                                    'copy_to': 'subjectAll.lt',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'nl': {
                                    'copy_to': 'subjectAll.nl',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'no': {
                                    'copy_to': 'subjectAll.no',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pl': {
                                    'copy_to': 'subjectAll.pl',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'pt': {
                                    'copy_to': 'subjectAll.pt',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ro': {
                                    'copy_to': 'subjectAll.ro',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'ru': {
                                    'copy_to': 'subjectAll.ru',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sk': {
                                    'copy_to': 'subjectAll.sk',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'sv': {
                                    'copy_to': 'subjectAll.sv',
                                    'fields': {'raw': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        }
                    },
                    'type': 'object'
                },
                'subjectAll': {
                    'properties': {
                        'bg': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'cs': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'da': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'de': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'el': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'es': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'fr': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'hu': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'it': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'lt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'nl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'no': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ro': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ru': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sk': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sv': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'object'
                },
                'subjectKeywords': {'type': 'keyword'},
                'title': {
                    'properties': {
                        'bg': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'cs': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'da': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'de': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'el': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'es': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'fr': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'hu': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'it': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'lt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'nl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'no': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pl': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pt': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ro': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ru': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sk': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sv': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'object'
                },
                'workIdentifiers': {
                    'properties': {
                        'RIV': {'type': 'keyword'},
                        'doi': {'type': 'keyword'},
                        'isbn': {'type': 'keyword'},
                        'issn': {'type': 'keyword'}
                    },
                    'type': 'object'
                }
            }
        }
    }
