# -*- coding: utf-8 -*-

"""
.. module:: prodiguer.db.dao_mq.py
   :copyright: Copyright "Apr 26, 2013", IPSL
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: MQ data access operations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from prodiguer import cv
from prodiguer.db import types, session



def _validate_create_term(
    term_type,
    term_name,
    term_display_name,
    ):
    """Validates create term inputs.

    """
    cv.validation.validate_term_type(term_type)
    cv.validation.validate_term_name(term_type, term_name)
    cv.validation.validate_term_display_name(term_display_name)


def create_term(
    term_type,
    term_name,
    term_display_name,
    ):
    """Creates a CV term in db.

    :param str term_type: Type of term being created.
    :param str term_name: Name of term being created.
    :param str term_display_name: Display name of term being created.

    :returns: Newly created CV term.
    :rtype: types.ControlledVocabularyTerm

    """
    # Validate inputs.
    _validate_create_term(
        term_type,
        term_name,
        term_display_name
        )

    # Instantiate instance.
    term = types.ControlledVocabularyTerm()
    term.typeof = term_type
    term.name = term_name
    term.display_name = term_display_name

    # Push to db.
    session.add(term)

    return term


def retrieve_term(term_type, term_name):
    """Returns a CV term from db.

    :param str term_type: Type of term being retrieved.
    :param str term_name: Name of term being retrieved.

    :returns: A CV term.
    :rtype: types.ControlledVocabularyTerm

    """
    qry = session.query(types.ControlledVocabularyTerm)
    qry = qry.filter(types.ControlledVocabularyTerm.typeof == unicode(term_type))
    qry = qry.filter(types.ControlledVocabularyTerm.name == unicode(term_name))

    return qry.first()