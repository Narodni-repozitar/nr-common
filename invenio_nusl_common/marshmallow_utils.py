def marshmallow_remove_required(schema):
    if hasattr(schema, "required"):
        schema.required = False
    if hasattr(schema, "validate"):
        setattr(schema, "validate", None)
    if hasattr(schema, "validators"):
        schema.validators.clear()
    if hasattr(schema, "_declared_fields"):
        for fld in getattr(schema, '_declared_fields', {}).values():
            marshmallow_remove_required(fld)
    elif hasattr(schema, "container"):
            marshmallow_remove_required(getattr(schema, 'container', {}))
    elif hasattr(schema, "nested"):
        marshmallow_remove_required(getattr(schema, 'nested', {}))

    return schema

#    if hasattr(schema, "_declared_fields"):
#        for fld in getattr(schema, '_declared_fields', {}).values():
#            inside()
#    elif hasattr(schema, "container"):
#        for fld in getattr(schema, 'container', {}).values():
#            inside()
#    elif hasattr(schema, "nested"):
#        for fld in getattr(schema, 'nested', {}).values():
#            inside()
#
# # if hasattr(fld, 'container'):
#    #     marshmallow_remove_required(fld.container)
#    # if hasattr(fld, 'nested'):
#    #     marshmallow_remove_required(fld.nested)
