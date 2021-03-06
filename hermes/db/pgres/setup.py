# -*- coding: utf-8 -*-

"""
.. module:: hermes.db.setup.py
   :platform: Unix
   :synopsis: Initializes database.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os
import uuid

from sqlalchemy.schema import CreateSchema
from sqlalchemy.schema import DropSchema

from hermes import cv
from hermes.db.pgres import session as db_session
from hermes.db.pgres.meta import METADATA
from hermes.db.pgres.types import ControlledVocabularyTerm
from hermes.db.pgres.types import Simulation
from hermes.db.pgres.types import SCHEMAS
from hermes.utils import convert
from hermes.utils import logger



def init_cv_terms():
    """Initialises set of cv terms.

    """
    logger.log_db("Inserting cv.tbl_cv_term records")

    for term in cv.io.read():
        item = ControlledVocabularyTerm()
        item.typeof = cv.get_type(term)
        item.name = cv.get_name(term)
        item.display_name = cv.get_display_name(term)
        item.synonyms = ", ".join(cv.get_synonyms(term)) or None
        item.uid = cv.get_uid(term)
        item.sort_key = cv.get_sort_key(term)
        db_session.insert(item)


def _init_simulations():
    """Initialises set of simulations.

    """
    logger.log_db("Inserting cnode.tbl_simulation records")

    # Set simulations from simulation.json file.
    fpath = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(fpath, "setup_data")
    fpath = os.path.join(fpath, "simulation.json")
    simulations = convert.json_file_to_dict(fpath)

    # Insert into db.
    for simulation in simulations:
        # ... ensure CV cross references are lower-case.
        for key in simulation['associations']:
            simulation['associations'][key] = simulation['associations'][key].lower()

        # ... hydrate new simulation;
        sim = Simulation()
        sim.accounting_project = u"cmip5"
        sim.compute_node = simulation['associations']['compute_node']
        sim.compute_node_login = simulation['associations']['compute_node_login']
        sim.compute_node_machine = simulation['associations']['compute_node_machine']
        sim.ensemble_member = simulation['ensemble_member']
        sim.execution_end_date = simulation['execution_end_date']
        sim.execution_start_date = simulation['execution_start_date']
        sim.experiment = simulation['associations']['experiment']
        sim.model = simulation['associations']['model']
        sim.name = simulation['name']
        sim.output_end_date = simulation['output_end_date']
        sim.output_start_date = simulation['output_start_date']
        sim.space = simulation['associations']['space']
        try:
            sim.parent_simulation_name = simulation['parent_simulation']
        except KeyError:
            pass
        try:
            sim.parent_simulation_branch_date = simulation['parent_simulation_branch_date']
        except KeyError:
            pass
        sim.uid = uuid.uuid4()

        # Set hash id.
        sim.hashid = sim.get_hashid()

        # ... insert into db.
        db_session.insert(sim)


def execute():
    """Sets up a database.

    """
    # Initialize schemas.
    db_session.sa_engine.execute(DropSchema('public'))
    for schema in SCHEMAS:
        db_session.sa_engine.execute(CreateSchema(schema))

    # Initialize tables.
    METADATA.create_all(db_session.sa_engine)

    # Seed tables.
    init_cv_terms()
    _init_simulations()
