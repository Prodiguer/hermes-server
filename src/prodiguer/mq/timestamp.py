# -*- coding: utf-8 -*-

"""
.. module:: prodiguer.mq.timestamp.py
   :copyright: Copyright "May 21, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A message timestamp wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import arrow


# Default timezone to apply.
_DEFAULT_TZ = 'Europe/Paris'


class Timestamp(object):
    """A timestamp generated by producer.

    """
    def __init__(self):
        """Object constructor.

        :param str raw: Raw timestamp generated by producer.

        """
        self.as_ms_float = None
        self.as_ms_int = None
        self.as_ms_raw = None
        self.as_ns_float = None
        self.as_ns_int = None
        self.as_ns_raw = None


    def __repr__(self):
        """Object string representation.

        """
        text = "ns_raw: {0}, ms_raw: {1}, ns_float: {2}, ms_float: {3}"

        return text.format(
            self.as_ns_raw, self.as_ms_raw, self.as_ns_float, self.as_ms_float)

    @property
    def as_ms(self):
        """Converts to microsecond precise datetime.datetime instance.

        """
        return arrow.get(self.as_ms_raw).to(_DEFAULT_TZ)


    @classmethod
    def from_ns(cls, as_ns_raw):
        """Creates an instance from a nano-second precise timestamp.

        :param str as_ns_raw: A nano-second precise timestamp.

        :returns: A timestamp wrapper instance.
        :rtype: Timestamp

        """
        # As ms precise raw string.
        as_ms_raw = "{0}T{1}.{2}+{3}".format(
            as_ns_raw.split("T")[0],
            as_ns_raw.split("T")[1].split("+")[0].split(".")[0],
            as_ns_raw.split("T")[1].split("+")[0].split(".")[1][:6],
            as_ns_raw.split("T")[1].split("+")[1])

        # As other ms precise values.
        as_ms = arrow.get(as_ms_raw).to(_DEFAULT_TZ)
        as_ms_float = "{0}.{1}".format(
            as_ms.timestamp,
            as_ms_raw.split("T")[1].split("+")[0].split(".")[1][:6])
        as_ms_int = int("".join(as_ms_float.split('.')))

        # As ns precise timestamp.
        as_ns_float = "{0}.{1}".format(
            as_ms.timestamp,
            as_ms_raw.split("T")[1].split("+")[0].split(".")[1])
        as_ns_int = int("".join(as_ns_float.split('.')))

        result = Timestamp()
        result.as_ms_float = as_ms_float
        result.as_ms_int = as_ms_int
        result.as_ms_raw = as_ms_raw
        result.as_ns_float = as_ns_float
        result.as_ns_int = as_ns_int
        result.as_ns_raw = as_ns_raw

        return result


    @classmethod
    def from_ms(cls, as_ms_raw):
        """Creates an instance from a micro-second precise timestamp.

        :param str as_ms_raw: A micro-second precise timestamp.

        :returns: A timestamp wrapper instance.
        :rtype: Timestamp

        """
        # As ns precise raw string.
        as_ns_raw = "{0}T{1}.{2}000+{3}".format(
            as_ms_raw.split("T")[0],
            as_ms_raw.split("T")[1].split("+")[0].split(".")[0],
            as_ms_raw.split("T")[1].split("+")[0].split(".")[1][:6],
            as_ms_raw.split("T")[1].split("+")[1])

        return Timestamp.from_ns(as_ns_raw)


def create(precision, raw):
    """Creates an instance from a raw timestamp.

    :param str precision: Timestamp precision.
    :param str raw: Raw timestamp.

    :returns: A timestamp wrapper instance.
    :rtype: mq.timestamp.Timestamp

    """
    if precision == "ms":
        return Timestamp.from_ms(raw)
    elif precision == "ns":
        return Timestamp.from_ns(raw)
    else:
        err = "Unsupported timestamp precision : {0}".format(precision)
        raise ValueError(err)
