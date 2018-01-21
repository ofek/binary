from __future__ import division

from collections import OrderedDict

BYTE = B = 1
KIBIBYTE = KB = BYTE * 1024
MEBIBYTE = MB = KIBIBYTE * 1024
GIBIBYTE = GB = MEBIBYTE * 1024
TEBIBYTE = TB = GIBIBYTE * 1024
PEBIBYTE = PB = TEBIBYTE * 1024
EXBIBYTE = EB = PEBIBYTE * 1024
ZEBIBYTE = ZB = EXBIBYTE * 1024
YOBIBYTE = YB = ZEBIBYTE * 1024

BINARY_PREFIX = OrderedDict((
    (BYTE, 'B'),
    (KIBIBYTE, 'KiB'),
    (MEBIBYTE, 'MiB'),
    (GIBIBYTE, 'GiB'),
    (TEBIBYTE, 'TiB'),
    (PEBIBYTE, 'PiB'),
    (EXBIBYTE, 'EiB'),
    (ZEBIBYTE, 'ZiB'),
    (YOBIBYTE, 'YiB'),
))


def convert_units(n, unit=BYTE, to=None):
    """Converts between IEC 80000-13:2008 units. If no ``unit`` is
    specified, ``n`` is assumed to already be in bytes. If no ``to`` is
    specified, ``n`` will be converted to the highest unit possible.

    Units conform to IEC standards, see:
    https://en.wikipedia.org/wiki/Binary_prefix
    https://en.wikipedia.org/wiki/IEC_80000-13
    https://www.iso.org/standard/31898.html (paywalled)

    :param n: The number of ``unit``\ s.
    :type n: ``int`` or ``float``
    :param unit: The unit ``n`` represents.
    :type unit: one of the global constants
    :param to: The unit to convert to.
    :type to: one of the global constants
    :returns: The unit pair, a numeric quantity and the unit's string.
    :rtype: tuple(quantity, string)
    """

    # Always work with bytes to simplify logic.
    n *= unit

    try:
        if to:
            return n / to, BINARY_PREFIX[to]
        elif n < KIBIBYTE:
            return n, BINARY_PREFIX[BYTE]
        elif n < MEBIBYTE:
            return n / KIBIBYTE, BINARY_PREFIX[KIBIBYTE]
        elif n < GIBIBYTE:
            return n / MEBIBYTE, BINARY_PREFIX[MEBIBYTE]
        elif n < TEBIBYTE:
            return n / GIBIBYTE, BINARY_PREFIX[GIBIBYTE]
        elif n < PEBIBYTE:
            return n / TEBIBYTE, BINARY_PREFIX[TEBIBYTE]
        elif n < EXBIBYTE:
            return n / PEBIBYTE, BINARY_PREFIX[PEBIBYTE]
        elif n < ZEBIBYTE:
            return n / EXBIBYTE, BINARY_PREFIX[EXBIBYTE]
        elif n < YOBIBYTE:
            return n / ZEBIBYTE, BINARY_PREFIX[ZEBIBYTE]
        else:
            return n / YOBIBYTE, BINARY_PREFIX[YOBIBYTE]
    except KeyError:
        raise ValueError('{} is not a valid binary unit.'.format(
            to if unit in BINARY_PREFIX else unit
        ))
