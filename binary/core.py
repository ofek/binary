from __future__ import division

from collections import namedtuple

BYTE = 1

# Binary
KIBIBYTE = BYTE * 1024
MEBIBYTE = KIBIBYTE * 1024
GIBIBYTE = MEBIBYTE * 1024
TEBIBYTE = GIBIBYTE * 1024
PEBIBYTE = TEBIBYTE * 1024
EXBIBYTE = PEBIBYTE * 1024
ZEBIBYTE = EXBIBYTE * 1024
YOBIBYTE = ZEBIBYTE * 1024

# SI
KILOBYTE = BYTE * 1000
MEGABYTE = KILOBYTE * 1000
GIGABYTE = MEGABYTE * 1000
TERABYTE = GIGABYTE * 1000
PETABYTE = TERABYTE * 1000
EXABYTE = PETABYTE * 1000
ZETTABYTE = EXABYTE * 1000
YOTTABYTE = ZETTABYTE * 1000

BINARY_PREFIXES = {
    BYTE: 'B',
    KIBIBYTE: 'KiB',
    MEBIBYTE: 'MiB',
    GIBIBYTE: 'GiB',
    TEBIBYTE: 'TiB',
    PEBIBYTE: 'PiB',
    EXBIBYTE: 'EiB',
    ZEBIBYTE: 'ZiB',
    YOBIBYTE: 'YiB',
}
DECIMAL_PREFIXES = {
    BYTE: 'B',
    KILOBYTE: 'KB',
    MEGABYTE: 'MB',
    GIGABYTE: 'GB',
    TERABYTE: 'TB',
    PETABYTE: 'PB',
    EXABYTE: 'EB',
    ZETTABYTE: 'ZB',
    YOTTABYTE: 'YB',
}

PREFIXES = BINARY_PREFIXES.copy()
PREFIXES.update(DECIMAL_PREFIXES)


BinaryUnits = namedtuple(
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
    BYTE, BYTE,
    KIBIBYTE, KIBIBYTE,
    MEBIBYTE, MEBIBYTE,
    GIBIBYTE, GIBIBYTE,
    TEBIBYTE, TEBIBYTE,
    PEBIBYTE, PEBIBYTE,
    EXBIBYTE, EXBIBYTE,
    ZEBIBYTE, ZEBIBYTE,
    YOBIBYTE, YOBIBYTE,
)
DecimalUnits = namedtuple(
    'DecimalUnits', (
        'BYTE', 'B',
        'KILOBYTE', 'KB',
        'MEGABYTE', 'MB',
        'GIGABYTE', 'GB',
        'TERABYTE', 'TB',
        'PETABYTE', 'PB',
        'EXABYTE', 'EB',
        'ZETTABYTE', 'ZB',
        'YOTTABYTE', 'YB',
    )
)(
    BYTE, BYTE,
    KILOBYTE, KILOBYTE,
    MEGABYTE, MEGABYTE,
    GIGABYTE, GIGABYTE,
    TERABYTE, TERABYTE,
    PETABYTE, PETABYTE,
    EXABYTE, EXABYTE,
    ZETTABYTE, ZETTABYTE,
    YOTTABYTE, YOTTABYTE,
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
    if unit not in PREFIXES:
        raise ValueError('{} is not a valid binary unit.'.format(unit))

    # Always work with bytes to simplify logic.
    n *= unit

    if to:
        try:
            return n / to, PREFIXES[to]
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
