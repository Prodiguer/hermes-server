# -*- coding: utf-8 -*-
"""
.. module:: utils.http_validator.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: HTTP request validation.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import json

import jsonschema

from hermes.web.utils import http_exceptions as exceptions
from hermes.web.schemas import get_schema



def validate_request(handler):
    """Validates request against mapped JSON schemas.

    :param utils.http.HTTPRequestHandler handler: An HTTP request handler.

    :raises: exceptions.SecurityError, exceptions.InvalidJSONSchemaError

    """
    _validate_request_headers(handler)
    _validate_request_params(handler)
    _validate_request_body(handler)


def _validate(handler, data, schema):
    """Validates data against a JSON schema.

    """
    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError as json_errors:
        raise exceptions.InvalidJSONSchemaError(json_errors)


def _validate_request_headers(handler):
    """Validates request headers against a JSON schema.

    """
    # Map request to schema.
    schema = get_schema('headers', handler.request.path)

    # Null case - escape.
    if schema is None:
        return

    # Validate request headers.
    _validate(handler, dict(handler.request.headers), schema)


def _validate_request_params(handler):
    """Validates request parameters against a JSON schema.

    """
    # Map request to schema.
    schema = get_schema('params', handler.request.path)

    # Null case.
    if schema is None:
        if handler.request.query_arguments:
            raise exceptions.SecurityError("Unexpected request url parameters.")

    # Validate request parameters.
    else:
        _validate(handler, handler.request.query_arguments, schema)


def _validate_request_body(handler):
    """Validates request body against a JSON schema.

    """
    # Map request to schema.
    schema = get_schema('body', handler.request.path)

    # Null case.
    if schema is None:
        if handler.request.body:
            # Temporary patch.
            handler.request.data = None
            return
            raise exceptions.SecurityError("Unexpected request body.")

    # Validate request data.
    else:
        # ... decode request data.
        data = json.loads(handler.request.body)

        # ... validate request data against schema.
        _validate(handler, data, schema)

        # ... append valid data to request.
        handler.request.data = data
