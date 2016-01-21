# -*- coding: utf-8 -*-

"""
.. module:: run_pgres_reset_env_metrics_table.py
   :copyright: Copyright "Mar 21, 2015", Institute Pierre Simon Laplace
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Resets prodiguer monitoring.tbl_environment_metric table.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from prodiguer.db import pgres as db
from prodiguer.utils import logger



def _main():
    """Main entry point.

    """
    logger.log_db("Reset environment metrics table begins")

    # Delete all records in table.
    with db.session.create(commitable=True):
        db.dao.delete_all(db.types.EnvironmentMetric)

    logger.log_db("Reset environment metrics table complete")


if __name__ == '__main__':
    _main()
