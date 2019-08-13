# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Schemas for marshmallow."""

from __future__ import absolute_import, print_function

from .json import ValueTypeSchemaV1, MultilanguageSchemaV1, OrganizationSchemaV1

__all__ = (
    'ValueTypeSchemaV1', 'MultilanguageSchemaV1', 'OrganizationSchemaV1')
