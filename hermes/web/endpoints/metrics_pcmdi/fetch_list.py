# -*- coding: utf-8 -*-
"""
.. module:: hermes.web.endpoints.metrics_pcmdi.list.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Simulation metric list group request handler.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from hermes.db.mongo import dao_metrics as dao
from hermes.web.request_validation import validator_metrics_pcmdi as rv
from hermes.web.utils.http import HermesHTTPRequestHandler



class FetchListRequestHandler(HermesHTTPRequestHandler):
    """Simulation list metric request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _set_output():
            """Sets response to be returned to client.

            """
            self.output = {
                'groups': dao.fetch_list()
            }

        def _set_headers():
            """Sets response headers to be returned to client.

            """
            self.set_header("Access-Control-Allow-Origin", "*")

        # Invoke tasks.
        self.invoke(rv.validate_fetch_list, [
            _set_output,
            _set_headers
            ])
