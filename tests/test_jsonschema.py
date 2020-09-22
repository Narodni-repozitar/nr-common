from invenio_jsonschemas import current_jsonschemas
from invenio_records.api import _records_state


def test_json(app, base_json):
    print("\n\n\n\n\n")
    print("START")
    print(app)
    print(current_jsonschemas.list_schemas())
    _records_state.validate(base_json, "https://nusl.cz/schemas/nusl-common-v1.0.0.json")
