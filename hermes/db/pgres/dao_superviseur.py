# -*- coding: utf-8 -*-

"""
.. module:: hermes.db.dao_superviseur.py
   :copyright: Copyright "Mar 21, 2015", IPSL
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Superviseur data access operations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from hermes.db.pgres import dao
from hermes.db.pgres import session
from hermes.db.pgres import types
from hermes.db.pgres import validator_dao_superviseur as validator
from hermes.utils import decorators



@decorators.validate(validator.validate_create_supervision)
def create_supervision(
    simulation_uid,
    job_uid,
    trigger_code
    ):
    """Creates a new supervision record in db.

    :param str simulation_uid: Simulation unique identifer.
    :param str job_uid: Job unique identifer.
    :param str trigger_code: Code explaining what caused the supervision act to be triggered.

    :returns: Newly created instance.
    :rtype: types.Supervision

    """
    instance = types.Supervision()
    instance.simulation_uid = unicode(simulation_uid)
    instance.job_uid = unicode(job_uid)
    instance.trigger_code = unicode(trigger_code)

    return session.insert(instance)


@decorators.validate(validator.validate_retrieve_supervision)
def retrieve_supervision(identifer):
    """Retrieves supervision details from db.

    :param str identifer: Supervision identifier.

    :returns: Supervision details.
    :rtype: types.Supervision

    """
    return dao.get_by_id(types.Supervision, identifer)

