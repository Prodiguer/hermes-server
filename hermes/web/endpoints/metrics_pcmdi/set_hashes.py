# -*- coding: utf-8 -*-

"""
.. module:: hermes.web.endpoints.metrics_pcmdi.rename.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Simulation metric group rename request handler.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from hermes.db.mongo import dao_metrics as dao
from hermes.web.request_validation import validator_metrics_pcmdi as rv
from hermes.web.utils.http import HermesHTTPRequestHandler



# Query parameter names.
_PARAM_GROUP = 'group'


class SetHashesRequestHandler(HermesHTTPRequestHandler):
    """Simulation metric group set hashes method request handler.

    """
    def post(self):
        """HTTP POST handler.

        """
        def _do_work(self):
            """Sets the hash identifiers for all metrics within the group.

            """
            dao.set_hashes(self.get_argument(_PARAM_GROUP))

        # Invoke tasks.
        self.invoke(rv.validate_set_hashes, _do_work)
