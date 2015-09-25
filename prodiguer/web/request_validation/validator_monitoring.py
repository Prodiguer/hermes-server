# -*- coding: utf-8 -*-

"""
.. module:: prodiguer.web.endpoints.sim_metrics.request_validator.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates simulation monitoring endpoint requests.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

from voluptuous import All, Required, Schema

from prodiguer.web.request_validation import validator as rv



# Query parameter names.
_PARAM_TIMESLICE = 'timeslice'
_PARAM_HASHID = 'hashid'
_PARAM_TRYID = 'tryID'
_PARAM_UID = 'uid'


def _MonitoringTimeslice():
    """Validates incoming simulation timeslice query parameter.

    """
    def func(val):
        """Inner function.

        """
        if val not in ['1W', '2W', '1M', '2M', '3M', '6M', '12M', 'ALL']:
            raise ValueError("Unsupported monitoring timeslice")

    return func


def validate_event(handler):
    """Validates event endpoint HTTP request.

    """
    # TODO
    pass


def validate_fetch_cv(handler):
    """Validates fetch_cv endpoint HTTP request.

    """
    rv.validate(handler)


def validate_fetch_all(handler):
    """Validates fetch_all endpoint HTTP request.

    """
    rv.validate(handler)


def validate_fetch_messages(handler):
    """Validates fetch_messages endpoint HTTP request.

    """
    def _query_validator(handler):
        """Validates HTTP request query arguments.

        """
        rv.validate_data(handler.request.query_arguments, {
            Required(_PARAM_UID): All(rv.Sequence(uuid.UUID))
            })

    rv.validate(handler, query_validator=_query_validator)


def validate_fetch_timeslice(handler):
    """Validates fetch_timeslice endpoint HTTP request.

    """
    def _query_validator(handler):
        """Validates HTTP request query arguments.

        """
        rv.validate_data(handler.request.query_arguments, {
            Required(_PARAM_TIMESLICE): All(rv.Sequence(str), _MonitoringTimeslice())
            })

    rv.validate(handler, query_validator=_query_validator)


def validate_fetch_one(handler):
    """Validates fetch_one endpoint HTTP request.

    """
    def _query_validator(handler):
        """Validates HTTP request query arguments.

        """
        rv.validate_data(handler.request.query_arguments, {
            Required(_PARAM_HASHID): All(rv.Sequence(str)),
            Required(_PARAM_TRYID): All(rv.Sequence(int))
            })

    rv.validate(handler, query_validator=_query_validator)


def validate_websocket(handler):
    """Validates websocket endpoint HTTP request.

    """
    rv.validate(handler)
