from decimal import Decimal
from typing import TYPE_CHECKING, NamedTuple, Optional, Tuple, Union

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


class _BinaryUnits(NamedTuple):
    BYTE: int
    B: int
    KIBIBYTE: int
    KB: int
    MEBIBYTE: int
    MB: int
    GIBIBYTE: int
    GB: int
    TEBIBYTE: int
    TB: int
    PEBIBYTE: int
    PB: int
    EXBIBYTE: int
    EB: int
    ZEBIBYTE: int
    ZB: int
    YOBIBYTE: int
    YB: int


BinaryUnits = _BinaryUnits(
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


class _DecimalUnits(NamedTuple):
    BYTE: int
    B: int
    KILOBYTE: int
    KB: int
    MEGABYTE: int
    MB: int
    GIGABYTE: int
    GB: int
    TERABYTE: int
    TB: int
    PETABYTE: int
    PB: int
    EXABYTE: int
    EB: int
    ZETTABYTE: int
    ZB: int
    YOTTABYTE: int
    YB: int


DecimalUnits = _DecimalUnits(
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


def convert_units(
    n: float,
    unit: int = BYTE,
    to: Optional[int] = None,
    si: bool = False,
    exact: bool = False
) -> Tuple[Union[float, Decimal], str]:
    r"""Converts between and within binary and decimal units. If no ``unit``
    is specified, ``n`` is assumed to already be in bytes. If no ``to`` is
    specified, ``n`` will be converted to the highest unit possible. If
    no ``unit`` nor ``to`` is specified, the output will be binary units
    unless ``si`` is ``True``. If ``exact`` is ``True``. the calculations
    will use decimal.Decimal.

    Binary units conform to IEC standards, see:
    https://en.wikipedia.org/wiki/Binary_prefix
    https://en.wikipedia.org/wiki/IEC_80000-13
    https://www.iso.org/standard/31898.html (paywalled)

    Decimal units conform to SI standards, see:
    https://en.wikipedia.org/wiki/International_System_of_Units

    :param n: The number of ``unit``s.
    :type n: ``int`` or ``float``
    :param unit: The unit ``n`` represents.
    :type unit: one of the global constants
    :param to: The unit to convert to.
    :type to: one of the global constants
    :param si: Assume SI units when no ``unit`` nor ``to`` is specified.
    :type si: ``bool``
    :param exact: Use decimal.Decimal for calculations.
    :type exact: ``bool``
    :returns: The unit pair: a numeric quantity and the unit's string.
    :rtype: tuple(quantity, string)
    """
    if unit not in PREFIXES:
        raise ValueError(f'{unit} is not a valid binary unit.')

    # Always work with bytes to simplify logic.
    b: Union[float, Decimal]
    if exact:
        b = Decimal(str(n)) * unit
    else:
        b = n * unit

    if to:
        try:
            return b // to if to == BYTE else b / to, PREFIXES[to]
        except KeyError:
            raise ValueError(f'{to} is not a valid unit.')

    babs = abs(b)
    if TYPE_CHECKING:
        assert isinstance(babs, float) or isinstance(babs, Decimal)

    if unit in BINARY_PREFIXES and not si:
        if babs < KIBIBYTE:
            return b, 'B'
        elif babs < MEBIBYTE:
            return b / KIBIBYTE, 'KiB'
        elif babs < GIBIBYTE:
            return b / MEBIBYTE, 'MiB'
        elif babs < TEBIBYTE:
            return b / GIBIBYTE, 'GiB'
        elif babs < PEBIBYTE:
            return b / TEBIBYTE, 'TiB'
        elif babs < EXBIBYTE:
            return b / PEBIBYTE, 'PiB'
        elif babs < ZEBIBYTE:
            return b / EXBIBYTE, 'EiB'
        elif babs < YOBIBYTE:
            return b / ZEBIBYTE, 'ZiB'
        else:
            return b / YOBIBYTE, 'YiB'
    else:
        if babs < KILOBYTE:
            return b, 'B'
        elif babs < MEGABYTE:
            return b / KILOBYTE, 'KB'
        elif babs < GIGABYTE:
            return b / MEGABYTE, 'MB'
        elif babs < TERABYTE:
            return b / GIGABYTE, 'GB'
        elif babs < PETABYTE:
            return b / TERABYTE, 'TB'
        elif babs < EXABYTE:
            return b / PETABYTE, 'PB'
        elif babs < ZETTABYTE:
            return b / EXABYTE, 'EB'
        elif babs < YOTTABYTE:
            return b / ZETTABYTE, 'ZB'
        else:
            return b / YOTTABYTE, 'YB'
