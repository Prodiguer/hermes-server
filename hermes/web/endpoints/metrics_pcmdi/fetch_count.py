# -*- coding: utf-8 -*-
"""
.. module:: hermes.web.endpoints.metrics_pcmdi.fetch_line_count.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Metric group line count request handler.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from hermes.db.mongo import dao_metrics as dao
from hermes.web.request_validation import validator_metrics_pcmdi as rv
from hermes.web.utils.http import HermesHTTPRequestHandler



# Supported content types.
_CONTENT_TYPE_JSON = ["application/json", "application/json; charset=UTF-8"]

# Query parameter names.
_PARAM_GROUP = 'group'


class FetchCountRequestHandler(HermesHTTPRequestHandler):
    """Simulation metric group fetch line count method request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _decode_request():
            """Decodes request.

            """
            self.group = self.get_argument(_PARAM_GROUP)
            self.query = self.decode_json_body(False)


        def _set_output():
            """Sets response to be returned to client.

            """
            self.output = {
                'group': self.group,
                'count': dao.fetch_count(self.group, self.query)
            }

        def _set_headers():
            """Sets response headers to be returned to client.

            """
            self.set_header("Access-Control-Allow-Origin", "*")


        def _cleanup():
            """Performs cleanup after request processing.

            """
            del self.group
            del self.query


        # Invoke tasks.
        self.invoke(rv.validate_fetch_count, [
            _decode_request,
            _set_output,
            _set_headers,
            _cleanup
        ])
