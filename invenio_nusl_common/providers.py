# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Thesis ID provider."""

from __future__ import absolute_import, print_function

from invenio_pidstore.models import PIDStatus
from invenio_pidstore.providers.base import BaseProvider

from invenio_nusl_common.models import NuslIdentifier


class NuslIdProvider(BaseProvider):
    """Thesss identifier provider."""

    pid_type = 'nusl'
    """Type of persistent identifier."""

    pid_provider = None
    """Provider name.

    The provider name is not recorded in the PID since the provider does not
    provide any additional features besides creation of record ids.
    """

    default_status = PIDStatus.RESERVED
    """Record IDs are by default registered immediately.

    Default: :attr:`invenio_pidstore.models.PIDStatus.RESERVED`
    """

    @classmethod
    def create(cls, object_type=None, object_uuid=None, **kwargs):
        """Create a new record identifier.

        Note: if the object_type and object_uuid values are passed, then the
        PID status will be automatically setted to
        :attr:`invenio_pidstore.models.PIDStatus.REGISTERED`.

        :param object_type: The object type. (Default: None.)
        :param object_uuid: The object identifier. (Default: None).
        :param kwargs: You specify the pid_value.
        """
        # Request next integer in recid sequence.
        assert 'pid_value' not in kwargs
        kwargs['pid_value'] = str(NuslIdentifier.next())
        kwargs.setdefault('status', cls.default_status)
        if object_type and object_uuid:
            kwargs['status'] = PIDStatus.REGISTERED
        return super(NuslIdProvider, cls).create(
            object_type=object_type, object_uuid=object_uuid, **kwargs)
