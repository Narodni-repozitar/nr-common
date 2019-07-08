import copy


def marshmallow_remove_required(schema):
    for fld in getattr(schema, '_declared_fields', {}).values():
        if fld.required:
            fld.required = False
        fld.validators.clear()
        if hasattr(fld, 'container'):
            marshmallow_remove_required(fld.container)
        if hasattr(fld, 'nested'):
            marshmallow_remove_required(fld.nested)
    return schema