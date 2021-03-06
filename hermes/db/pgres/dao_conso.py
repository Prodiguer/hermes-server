# -*- coding: utf-8 -*-

"""
.. module:: hermes.db.dao_conso.py
   :copyright: Copyright "Mar 21, 2015", IPSL
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: CONSO data access operations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import arrow

from hermes.db.pgres import session
from hermes.db.pgres import types
from hermes.db.pgres import validator_dao_conso as validator
from hermes.utils import decorators



@decorators.validate(validator.validate_persist_allocation)
def persist_allocation(
    centre,
    project,
    sub_project,
    machine,
    node_type,
    start_date,
    end_date,
    total_hrs,
    is_active,
    is_reviewed
    ):
    """Persists allocation information to db.

    :param str centre: HPC, e.g. TGCC.
    :param str project: Accounting project, e.g. gencmip6.
    :param str sub_project: Accounting sub-project, e.g. devcmip6.
    :param str machine: HPC machine, e.g. curie.
    :param str node_type: HPC node type, e.g. thin/standard.
    :param datetime start_date: Allocation start date.
    :param datetime end_date: Allocation end date.
    :param float total_hrs: Total allocated compute time.
    :param boolean is_active: Flag indicating whether the allocation is active or not.
    :param boolean is_reviewed: Flag indicating whether the allocation is reviewed or not.

    :returns: A new allocation instance.
    :rtype: types.Allocation

    """
    instance = types.Allocation()
    instance.centre = unicode(centre)
    instance.project = unicode(project)
    instance.sub_project = unicode(sub_project) if sub_project else None
    instance.machine = unicode(machine)
    instance.node_type = unicode(node_type)
    instance.start_date = start_date
    instance.end_date = end_date
    instance.total_hrs = float(total_hrs)
    instance.is_active = bool(is_active)
    instance.is_reviewed = bool(is_reviewed)

    return session.insert(instance)


@decorators.validate(validator.validate_retrieve_allocation)
def retrieve_allocation(
    centre,
    project,
    machine,
    node_type,
    consumption_date
    ):
    """Retrieves allocation information from db.

    :param str centre: HPC, e.g. TGCC.
    :param str project: Accounting project, e.g. ra2641.
    :param str machine: HPC machine, e.g. curie.
    :param str node_type: HPC node type, e.g. thin/standard.
    :param datetime consumption_date: Data upon which resource consumption occurred.

    :returns: An allocation instance if found else None.
    :rtype: types.Allocation | None

    """
    a = types.Allocation

    qry = session.query(a)
    qry = qry.filter(a.centre == unicode(centre))
    qry = qry.filter(a.project == unicode(project))
    qry = qry.filter(a.machine == unicode(machine))
    qry = qry.filter(a.node_type == unicode(node_type))
    qry = qry.filter(a.start_date <= consumption_date)
    qry = qry.filter(a.end_date >= consumption_date)

    return qry.first()


@decorators.validate(validator.validate_persist_consumption)
def persist_consumption(
    allocation_id,
    date,
    total_hrs,
    login=None,
    sub_project=None,
    batch_date=None
    ):
    """Persists consumption into db.

    :param int allocation_id: ID of associated allocation.
    :param datetime date: Comsumption date.
    :param float total_hours: Consumption total hours.
    :param str login: User login.
    :param str sub_project: Accounting sub-project, e.g. devcmip6.
    :param datetime batch_date: Date upon which associated consumption batch was persisted.

    :returns: A new consumption instance.
    :rtype: types.Consumption

    """
    instance = types.Consumption()
    instance.allocation_id = allocation_id
    instance.date = arrow.get(date).datetime
    instance.total_hrs = float(total_hrs)
    if sub_project is not None:
        instance.sub_project = unicode(sub_project)
    if login is not None:
        instance.login = unicode(login)
    if batch_date is not None:
        instance.row_create_date = batch_date

    return session.insert(instance)


@decorators.validate(validator.validate_retrieve_consumption_header)
def retrieve_consumption_header(allocation_id, date):
    """Retrieves consumption header from db.

    :param int allocation_id: ID of associated allocation.
    :param datetime date: Comsumption date.

    :returns: A consumption instance if found else None.
    :rtype: types.Consumption | None

    """
    c = types.Consumption

    qry = session.query(c)
    qry = qry.filter(c.allocation_id == allocation_id)
    qry = qry.filter(c.date == date)

    return qry.first()
