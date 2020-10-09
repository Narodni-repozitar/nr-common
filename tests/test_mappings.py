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
        'aliases': {
          'nr-all':{}
        },
        'mappings': {
            'date_detection': False,
            'dynamic': False,
            'numeric_detection': False,
            'properties': {
                '$schema': {'index': True, 'type': 'keyword'},
                'abstract': {
                    'properties': {
                        'cs': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'object'
                },
                'accessRights': {
                    'properties': {
                        'is_ancestor': {'type': 'boolean'},
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
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
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
                        'cs': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
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
                            'type': 'text'
                        },
                        'researcherID': {'type': 'keyword'},
                        'role': {
                            'properties': {
                                'dataCiteCode': {'type': 'keyword'},
                                'is_ancestor': {'type': 'boolean'},
                                'links': {
                                    'properties': {
                                        'parent': {'type': 'keyword'},
                                        'self': {'type': 'keyword'}
                                    },
                                    'type': 'object'
                                },
                                'marcCode': {'type': 'keyword'}
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
                            'type': 'text'
                        },
                        'researcherID': {'type': 'keyword'},
                        'scopusID': {'type': 'keyword'},
                        'vedidk': {'type': 'keyword'}
                    },
                    'type': 'nested'
                },
                'dateIssued': {'type': 'keyword'},
                'dateModified': {'type': 'keyword'},
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
                        'cs': {
                            'copy_to': 'subjectKeyword',
                            'type': 'keyword'
                        },
                        'en': {
                            'copy_to': 'subjectKeyword',
                            'type': 'keyword'
                        }
                    },
                    'type': 'object'
                },
                'language': {
                    'properties': {
                        'is_ancestor': {'type': 'boolean'},
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'title': {
                            'properties': {
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
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
                        'url': {'type': 'keyword'}
                    },
                    'type': 'object'
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
                        'url': {'type': 'keyword'}
                    },
                    'type': 'object'
                },
                'publicationPlace': {
                    'properties': {
                        'country': {
                            'properties': {
                                'is_ancestor': {'type': 'boolean'},
                                'links': {
                                    'properties': {
                                        'parent': {'type': 'keyword'},
                                        'self': {'type': 'keyword'}
                                    },
                                    'type': 'object'
                                },
                                'title': {
                                    'properties': {
                                        'cs': {
                                            'fields': {'keywords': {'type': 'keyword'}},
                                            'type': 'text'
                                        },
                                        'en': {
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
                        'itemRelationship': {
                            'properties': {
                                'is_ancestor': {'type': 'boolean'},
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
                        'links': {
                            'properties': {
                                'parent': {'type': 'keyword'},
                                'self': {'type': 'keyword'}
                            },
                            'type': 'object'
                        },
                        'title': {
                            'properties': {
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
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
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        }
                    },
                    'type': 'object'
                },
                'series': {
                    'properties': {
                        'name': {
                            'fields': {'keyword': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'volume': {'type': 'keyword'}
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
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        },
                        'is_ancestor': {'type': 'boolean'},
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
                                'cs': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                },
                                'en': {
                                    'fields': {'keywords': {'type': 'keyword'}},
                                    'type': 'text'
                                }
                            },
                            'type': 'object'
                        }
                    },
                    'type': 'object'
                },
                'subjectKeywords': {'type': 'keyword'},
                'title': {
                    'properties': {
                        'cs': {
                            'fields': {'keywords': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
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
