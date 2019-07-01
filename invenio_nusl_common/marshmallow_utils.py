import copy


def marshmallow_remove_required(schema, deep_copy=True):
    if deep_copy:
        schema = copy.deepcopy(schema)
    for fld in getattr(schema, '_declared_fields', {}).values():
        if fld.required:
            fld.required = False
        if hasattr(fld, 'container'):
            marshmallow_remove_required(fld.container, deep_copy=False)
        if hasattr(fld, 'nested'):
            marshmallow_remove_required(fld.nested, deep_copy=False)
