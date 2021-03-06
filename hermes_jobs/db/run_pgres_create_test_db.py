# -*- coding: utf-8 -*-

"""
.. module:: run_pgres_create_test_db.py
   :copyright: Copyright "Mar 21, 2015", Institute Pierre Simon Laplace
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Creates a test database that simulates a years worth of simulations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import base64
import datetime
import json
import os
import random
import uuid

import arrow

from hermes import cv
from hermes import mq
from hermes.db import pgres as db
from hermes.utils import config
from hermes.utils import logger



# Number of days for which to create test simulations.
_QUOTA_DAYS = 2

# Number of simulations to create per day.
_QUOTA_SIMS_PER_DAY = 30

# Number of jobs to create per simulation.
_QUOTA_JOBS_PER_SIM = 30

# Number of messages to create per day.
_QUOTA_MSG_PER_JOB = 10

# Set of accounting projects to be used.
_ACCOUNTING_PROJECTS = [
    u"ipsl",
    u"lmd",
    u"gencmip6",
    u"gen1000",
    u"gen2000",
    u"gen3000",
    u"gen4000",
    u"gen5000",
    u"gen6000",
    u"gen7000",
    u"gen8000",
    u"gen9000",
]

# The global now.
_NOW = datetime.datetime.utcnow()

# Set of output end/start data to be used.
_OUTPUT_DATES = [datetime.datetime(1880 + (i * 10), 1, 1) for i in range(15)]

# Default post processing date.
PP_DATE = arrow.get("20100101", "YYYYMMDD").datetime

# Set of job types.
_JOB_TYPESET = [
    u"c",
    u"p"
]

# Simulation configuration card.
_CONFIG_CARD = None

# Set of job types.
_POST_PROCESSING_JOB_NAMES = [
    u"monitoring",
    unicode(uuid.uuid4())[0:15],
    unicode(uuid.uuid4())[0:15],
    unicode(uuid.uuid4())[0:15],
    unicode(uuid.uuid4())[0:15],
    unicode(uuid.uuid4())[0:15],
    unicode(uuid.uuid4())[0:15],
    unicode(uuid.uuid4())[0:15],
]


def _get_cv_term(term_type):
    """Get a test cv term.

    """
    name = ''
    while len(name) == 0:
        name = cv.get_name(cv.cache.get_random_term(term_type))

    return name


def _create_job(simulation, job_index):
    """Create a test job.

    """
    typeof = random.choice(_JOB_TYPESET)
    if typeof == "p":
        pp_date = PP_DATE
        pp_name = random.choice(_POST_PROCESSING_JOB_NAMES)
    else:
        pp_date = None
        pp_name = None

    instance = db.types.Job()
    instance.simulation_uid = simulation.uid
    instance.job_uid = unicode(uuid.uuid4())
    instance.accounting_project = simulation.accounting_project
    instance.execution_start_date = simulation.execution_start_date + datetime.timedelta(hours=job_index * 2)
    if job_index == _QUOTA_JOBS_PER_SIM - 1:
        instance.execution_end_date = simulation.execution_start_date
    else:
        instance.execution_end_date = instance.execution_start_date + datetime.timedelta(hours=1)
    instance.is_error = False
    instance.is_compute_end = False
    instance.is_im = (pp_name == 'monitoring')
    instance.scheduler_id = random.randint(2000000, 9000000)
    instance.submission_path = unicode(uuid.uuid4())
    instance.post_processing_name = pp_name
    instance.post_processing_date = PP_DATE
    instance.post_processing_dimension = None
    instance.post_processing_component = None
    instance.post_processing_file = None
    instance.typeof = typeof
    instance.warning_delay = config.apps.monitoring.defaultJobWarningDelayInSeconds

    return db.session.insert(instance)


def _create_simulation_configuration(simulation):
    """Create a test simulation configuration card.

    """
    global _CONFIG_CARD

    if _CONFIG_CARD is None:
        fpath = os.path.abspath(__file__).replace('.py', '.txt')
        with open(fpath, 'r') as f:
            _CONFIG_CARD = f.read()
            _CONFIG_CARD = base64.encodestring(_CONFIG_CARD)

    instance = db.types.SimulationConfiguration()
    instance.simulation_uid = simulation.uid
    instance.card = _CONFIG_CARD

    return db.session.insert(instance)


def _create_simulation(start_date, end_date):
    """Create a test simulation.

    """
    compute_node_machine = _get_cv_term(cv.constants.TERM_TYPE_COMPUTE_NODE_MACHINE)
    compute_node = compute_node_machine.split("-")[0]

    instance = db.types.Simulation()
    instance.accounting_project = random.choice(_ACCOUNTING_PROJECTS)
    instance.compute_node = compute_node
    instance.compute_node_login = _get_cv_term(cv.constants.TERM_TYPE_COMPUTE_NODE_LOGIN)
    instance.compute_node_machine = compute_node_machine
    instance.experiment = _get_cv_term(cv.constants.TERM_TYPE_EXPERIMENT)
    instance.is_error = False
    instance.is_obsolete = False
    instance.execution_start_date = start_date
    instance.execution_end_date = end_date
    instance.model = _get_cv_term(cv.constants.TERM_TYPE_MODEL)
    instance.name = unicode(uuid.uuid4())[0:15]
    instance.output_start_date = random.choice(_OUTPUT_DATES)
    instance.output_end_date = instance.output_start_date + datetime.timedelta(days=365)
    instance.space = _get_cv_term(cv.constants.TERM_TYPE_SIMULATION_SPACE)
    instance.try_id = 1
    instance.uid = unicode(uuid.uuid4())
    instance.hashid = instance.get_hashid()

    return db.session.insert(instance)


def _create_job_message(simulation, job, message_type):
    """Create test message related to a simulation job.

    """
    instance = db.types.Message()
    instance.app_id = unicode(mq.constants.APP_MONITORING)
    instance.producer_id = unicode(mq.constants.PRODUCER_HERMES)
    instance.producer_version = u"x.x.x"
    instance.type_id = message_type
    instance.user_id = mq.constants.USER_HERMES
    instance.uid = unicode(uuid.uuid4())
    instance.correlation_id_1 = simulation.uid
    instance.correlation_id_2 = job.job_uid
    instance.content = json.dumps({
        "accountingProject": job.accounting_project,
        "jobuid": job.job_uid,
        "jobSchedulerID": job.scheduler_id,
        "jobWarningDelay": job.warning_delay,
        "jobSubmissionPath": job.submission_path,
        "simuid": simulation.uid
    })

    if message_type == mq.constants.MESSAGE_TYPE_0000:
        instance.timestamp = simulation.execution_start_date
    elif message_type == mq.constants.MESSAGE_TYPE_0100:
        instance.timestamp = simulation.execution_end_date
    instance.timestamp_raw = unicode(instance.timestamp)

    return db.session.insert(instance)


def _create_simulation_messages(s):
    return



def _create_simulation_jobs(s):
    jobs = [_create_job(s, i) for i in range(_QUOTA_JOBS_PER_SIM)]

    print s.execution_start_date, jobs[0].execution_start_date
    # print s.execution_start_date, jobs[10].execution_start_date
    # print s.execution_end_date, jobs[10].execution_end_date
    print s.execution_end_date, jobs[-1].execution_start_date
    print "------------------------------"

    s.jobs = jobs


def _main():
    """Main entry point.

    """
    # Initialize.
    then = arrow.utcnow()
    cv.cache.load()

    # Create N simulations per day for the last M days.
    for start_date in (_NOW - datetime.timedelta(days=x) for x in xrange(_QUOTA_DAYS, 1, -1)):
        logger.log_db("creating {} simulations starting at: {}".format(_QUOTA_SIMS_PER_DAY, start_date))
        end_date = start_date + datetime.timedelta(days=4)
        for _ in range(_QUOTA_SIMS_PER_DAY):
            s = _create_simulation(start_date, end_date)
            _create_simulation_configuration(s)
            _create_simulation_jobs(s)
            # _create_simulation_messages(s)



    # Finalize.
    msg = "created {} simulations in: {}"
    msg = msg.format(_QUOTA_DAYS * _QUOTA_SIMS_PER_DAY, arrow.utcnow() - then)
    logger.log_db(msg)


if __name__ == '__main__':
    with db.session.create(commitable=True):
        _main()
