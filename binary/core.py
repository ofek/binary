from __future__ import division

from collections import OrderedDict, namedtuple

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


units = namedtuple(
    'BinaryUnits', (
        'BYTE', 'B',
        'KIBIBYTE', 'KB',
        'MEBIBYTE', 'MB',
        'GIBIBYTE', 'GB',
        'TEBIBYTE', 'TB',
        'PEBIBYTE', 'PB',
        'EXBIBYTE', 'EB',
        'ZEBIBYTE', 'ZB',
        'YOBIBYTE', 'YB',
    )
)(
    BYTE, B,
    KIBIBYTE, KB,
    MEBIBYTE, MB,
    GIBIBYTE, GB,
    TEBIBYTE, TB,
    PEBIBYTE, PB,
    EXBIBYTE, EB,
    ZEBIBYTE, ZB,
    YOBIBYTE, YB,
)


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
    :returns: The unit pair: a numeric quantity and the unit's string.
    :rtype: tuple(quantity, string)
    """
    if unit not in BINARY_PREFIX:
        raise ValueError('{} is not a valid binary unit.'.format(unit))

    # Always work with bytes to simplify logic.
    n *= unit

    if to:
        try:
            return n / to, BINARY_PREFIX[to]
        except KeyError:
            raise ValueError('{} is not a valid binary unit.'.format(to))
    elif n < KIBIBYTE:
        return n, 'B'
    elif n < MEBIBYTE:
        return n / KIBIBYTE, 'KiB'
    elif n < GIBIBYTE:
        return n / MEBIBYTE, 'MiB'
    elif n < TEBIBYTE:
        return n / GIBIBYTE, 'GiB'
    elif n < PEBIBYTE:
        return n / TEBIBYTE, 'TiB'
    elif n < EXBIBYTE:
        return n / PEBIBYTE, 'PiB'
    elif n < ZEBIBYTE:
        return n / EXBIBYTE, 'EiB'
    elif n < YOBIBYTE:
        return n / ZEBIBYTE, 'ZiB'
    else:
        return n / YOBIBYTE, 'YiB'
