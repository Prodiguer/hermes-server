# -*- coding: utf-8 -*-

"""
.. module:: cv.session.py
   :copyright: Copyright "December 01, 2014", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Controlled vocabulary session manager.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections

from hermes.cv import accessor as ta
from hermes.cv import cache
from hermes.cv import constants
from hermes.cv import io
from hermes.utils import logger



# Session state.
_STATE = collections.defaultdict(list)


def _do(data, action):
    """Executes an action over cv data.

    """
    if not data:
        return

    terms = [data] if isinstance(data, collections.Mapping) else data

    return [action(term) for term in terms]


def init():
    """Initializes a CV session.

    """
    cache.load()
    logger.log_cv("initialized CV session ...")


def commit():
    """Commits CV session changes.

    """
    # Escape when there is nothing to commit.
    if not _STATE["destructions"] and \
       not _STATE["insertions"] and \
       not _STATE["deletions"]:
        return

    for term in _STATE["destructions"]:
        io.delete(term)
        cache.remove_term(term)
        logger.log_cv("Destroyed term: {}".format(ta.get_repr(term)))
    for term in _STATE["insertions"]:
        io.write(term)
        cache.add_term(term)
        logger.log_cv("Inserted term: {}".format(ta.get_repr(term)))
    for term in _STATE["deletions"]:
        io.write(term)
        cache.remove_term(term)
        logger.log_cv("Deleted term: {}".format(ta.get_repr(term)))

    logger.log_cv("Session updates committed to file system")

    _STATE.clear()


def insert(data):
    """Marks a previously created term for creation.

    :param obj data: Either a term or collection to be inserted.

    """
    def _insert(term):
        """Processes a term.

        """
        _STATE["insertions"].append(term)

    return _do(data, _insert)


def delete(data):
    """Marks a term for deletion.

    :param obj data: Either a term or collection to be deleted.

    """
    def _delete(term):
        """Processes a term.

        """
        ta.set_status(term, constants.TERM_GOVERNANCE_STATE_DELETED)
        ta.set_update_date(term)
        _STATE["deletions"].append(term)

    _do(data, _delete)


def destroy(data):
    """Marks a term for desctruction.

    :param obj data: Either a term or collection to be destroyed.

    """
    def _destroy(term):
        """Processes a term.

        """
        ta.set_status(term, constants.TERM_GOVERNANCE_STATE_DESTROYED)
        ta.set_update_date(term)
        _STATE["destructions"].append(term)

    _do(data, _destroy)
