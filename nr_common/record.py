from flask import url_for
from invenio_records.api import Record
from oarepo_references.mixins import ReferenceEnabledRecordMixin
from oarepo_validate import SchemaKeepingRecordMixin, MarshmallowValidatedRecordMixin

from .constants import COMMON_ALLOWED_SCHEMAS, COMMON_PREFERRED_SCHEMA
from .marshmallow import CommonMetadataSchemaV2


class PublishedCommonRecord(SchemaKeepingRecordMixin,
                            MarshmallowValidatedRecordMixin,
                            ReferenceEnabledRecordMixin,
                            Record):
    ALLOWED_SCHEMAS = COMMON_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = COMMON_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = CommonMetadataSchemaV2

    @property
    def canonical_url(self):
        return url_for('invenio_records_rest.common_item',
                       pid_value=self['control_number'], _external=True)
