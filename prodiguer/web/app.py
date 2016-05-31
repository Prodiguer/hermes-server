# -*- coding: utf-8 -*-

"""
.. module:: hermes.web.app.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Web service application entry point.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado
from tornado.web import Application


import prodiguer
from prodiguer.web.endpoints import aggregations
from prodiguer.web.endpoints import cv
from prodiguer.web.endpoints import monitoring
from prodiguer.web.endpoints import ops
from prodiguer.web.endpoints import sim_metrics
from prodiguer.web.utils import websockets
from prodiguer.utils import config
from prodiguer.utils import logger
from prodiguer.utils import shell



# Base address to API endpoints.
_BASE_ADDRESS = '{0}/api/1{1}'


def _get_path_to_front_end():
    """Return path to the front end javascript application.

    """
    dir_fe = shell.get_repo_path(['hermes-fe', 'src'])
    logger.log_web("Front-end static files @ {0}".format(dir_fe))

    return dir_fe


def _get_app_routes():
    """Returns supported app routes.

    """
    return (
        # Aggregation routes.
        # (r'/api/1/aggregations/find', aggregations.FindRequestHandler),
        # Controlled vocabulary routes.
        (r'/api/1/cv/fetch',
            cv.FetchRequestHandler),
        # Simulation monitoring routes.
        (r'/api/1/simulation/monitoring/fetch_detail',
            monitoring.FetchDetailRequestHandler),
        (r'/api/1/simulation/monitoring/fetch_messages',
            monitoring.FetchMessagesRequestHandler),
        (r'/api/1/simulation/monitoring/fetch_timeslice',
            monitoring.FetchTimeSliceRequestHandler),
        (r'/api/1/simulation/monitoring/ws/all',
            monitoring.FrontEndWebSocketAllHandler),
        (r'/api/1/simulation/monitoring/event',
            monitoring.EventRequestHandler),
        # Simulation metric routes.
        (r'/api/1/simulation/metrics/add',
            sim_metrics.AddRequestHandler),
        (r'/api/1/simulation/metrics/delete',
            sim_metrics.DeleteRequestHandler),
        (r'/api/1/simulation/metrics/fetch',
            sim_metrics.FetchRequestHandler),
        (r'/api/1/simulation/metrics/fetch_count',
            sim_metrics.FetchCountRequestHandler),
        (r'/api/1/simulation/metrics/fetch_columns',
            sim_metrics.FetchColumnsRequestHandler),
        (r'/api/1/simulation/metrics/fetch_list',
            sim_metrics.FetchListRequestHandler),
        (r'/api/1/simulation/metrics/fetch_setup',
            sim_metrics.FetchSetupRequestHandler),
        (r'/api/1/simulation/metrics/rename',
            sim_metrics.RenameRequestHandler),
        (r'/api/1/simulation/metrics/set_hashes',
            sim_metrics.SetHashesRequestHandler),
        # Operations routes.
        (r'/api',
            ops.HeartbeatRequestHandler),
        (r'/api/1/ops/heartbeat',
            ops.HeartbeatRequestHandler)
    )


def _get_app_settings():
    """Returns app settings.

    """
    return {
        "cookie_secret": config.web.cookie_secret,
        "compress_response": True,
        "static_path": _get_path_to_front_end()
    }


def _is_in_debug_mode():
    """Returns app debug mode.

    """
    return config.deploymentMode == 'dev'


def get_endpoint(suffix):
    """Returns the endpoint prefixed with base address.

    :param str suffix: Endpoint suffix.

    :returns: The endpoint prefixed with base address.
    :rtype: str

    """
    return _BASE_ADDRESS.format(config.web.url, suffix)


def run():
    """Runs the prodiguer web api.

    """
    # Setup app.
    logger.log_web("Initializing")

    # Initialise cv session.
    prodiguer.cv.session.init()

    # Instantiate.
    app = Application(_get_app_routes(),
                      debug=_is_in_debug_mode(),
                      **_get_app_settings())

    # Listen.
    app.listen(config.web.port)

    # Set web-socket keep alive.
    websockets.keep_alive()

    # Start io loop.
    logger.log_web("Ready")
    tornado.ioloop.IOLoop.instance().start()



# Main entry point.
if __name__ == '__main__':
    run()

