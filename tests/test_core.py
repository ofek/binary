from __future__ import division

import pytest

import binary
from binary import (
    BinaryUnits as bunits, DecimalUnits as dunits, convert_units
)
from binary.core import PREFIXES


class TestConstants:
    def test_byte(self):
        assert binary.BYTE == bunits.BYTE == bunits.B == 1
        assert binary.BYTE == dunits.BYTE == dunits.B == 1

    def test_kibibyte(self):
        assert binary.KIBIBYTE == bunits.KIBIBYTE == bunits.KB == 1024 ** 1

    def test_mebibyte(self):
        assert binary.MEBIBYTE == bunits.MEBIBYTE == bunits.MB == 1024 ** 2

    def test_gibibyte(self):
        assert binary.GIBIBYTE == bunits.GIBIBYTE == bunits.GB == 1024 ** 3

    def test_tebibyte(self):
        assert binary.TEBIBYTE == bunits.TEBIBYTE == bunits.TB == 1024 ** 4

    def test_pebibyte(self):
        assert binary.PEBIBYTE == bunits.PEBIBYTE == bunits.PB == 1024 ** 5

    def test_exbibyte(self):
        assert binary.EXBIBYTE == bunits.EXBIBYTE == bunits.EB == 1024 ** 6

    def test_zebibyte(self):
        assert binary.ZEBIBYTE == bunits.ZEBIBYTE == bunits.ZB == 1024 ** 7

    def test_yobibyte(self):
        assert binary.YOBIBYTE == bunits.YOBIBYTE == bunits.YB == 1024 ** 8

    def test_kilobyte(self):
        assert binary.KILOBYTE == dunits.KILOBYTE == dunits.KB == 1000 ** 1

    def test_megabyte(self):
        assert binary.MEGABYTE == dunits.MEGABYTE == dunits.MB == 1000 ** 2

    def test_gigabyte(self):
        assert binary.GIGABYTE == dunits.GIGABYTE == dunits.GB == 1000 ** 3

    def test_terabyte(self):
        assert binary.TERABYTE == dunits.TERABYTE == dunits.TB == 1000 ** 4

    def test_petabyte(self):
        assert binary.PETABYTE == dunits.PETABYTE == dunits.PB == 1000 ** 5

    def test_exabyte(self):
        assert binary.EXABYTE == dunits.EXABYTE == dunits.EB == 1000 ** 6

    def test_zettabyte(self):
        assert binary.ZETTABYTE == dunits.ZETTABYTE == dunits.ZB == 1000 ** 7

    def test_yottabyte(self):
        assert binary.YOTTABYTE == dunits.YOTTABYTE == dunits.YB == 1000 ** 8


class TestAccurateString:
    def test_byte(self):
        assert PREFIXES[bunits.BYTE] == 'B'
        assert PREFIXES[dunits.BYTE] == 'B'

    def test_kibibyte(self):
        assert PREFIXES[bunits.KIBIBYTE] == 'KiB'

    def test_mebibyte(self):
        assert PREFIXES[bunits.MEBIBYTE] == 'MiB'

    def test_gibibyte(self):
        assert PREFIXES[bunits.GIBIBYTE] == 'GiB'

    def test_tebibyte(self):
        assert PREFIXES[bunits.TEBIBYTE] == 'TiB'

    def test_pebibyte(self):
        assert PREFIXES[bunits.PEBIBYTE] == 'PiB'

    def test_exbibyte(self):
        assert PREFIXES[bunits.EXBIBYTE] == 'EiB'

    def test_zebibyte(self):
        assert PREFIXES[bunits.ZEBIBYTE] == 'ZiB'

    def test_yobibyte(self):
        assert PREFIXES[bunits.YOBIBYTE] == 'YiB'

    def test_kilobyte(self):
        assert PREFIXES[dunits.KILOBYTE] == 'KB'

    def test_megabyte(self):
        assert PREFIXES[dunits.MEGABYTE] == 'MB'

    def test_gigabyte(self):
        assert PREFIXES[dunits.GIGABYTE] == 'GB'

    def test_terabyte(self):
        assert PREFIXES[dunits.TERABYTE] == 'TB'

    def test_petabyte(self):
        assert PREFIXES[dunits.PETABYTE] == 'PB'

    def test_exabyte(self):
        assert PREFIXES[dunits.EXABYTE] == 'EB'

    def test_zettabyte(self):
        assert PREFIXES[dunits.ZETTABYTE] == 'ZB'

    def test_yottabyte(self):
        assert PREFIXES[dunits.YOTTABYTE] == 'YB'


class TestConvert:
    def test_byte(self):
        assert convert_units(1, bunits.YB, bunits.B) == (bunits.YB / 1, 'B')
        assert convert_units(1, dunits.YB, dunits.B) == (dunits.YB / 1, 'B')

    def test_kibibyte(self):
        assert convert_units(1, bunits.YB, bunits.KB) == (bunits.YB / 1024 ** 1, 'KiB')

    def test_mebibyte(self):
        assert convert_units(1, bunits.YB, bunits.MB) == (bunits.YB / 1024 ** 2, 'MiB')

    def test_gibibyte(self):
        assert convert_units(1, bunits.YB, bunits.GB) == (bunits.YB / 1024 ** 3, 'GiB')

    def test_tebibyte(self):
        assert convert_units(1, bunits.YB, bunits.TB) == (bunits.YB / 1024 ** 4, 'TiB')

    def test_pebibyte(self):
        assert convert_units(1, bunits.YB, bunits.PB) == (bunits.YB / 1024 ** 5, 'PiB')

    def test_exbibyte(self):
        assert convert_units(1, bunits.YB, bunits.EB) == (bunits.YB / 1024 ** 6, 'EiB')

    def test_zebibyte(self):
        assert convert_units(1, bunits.YB, bunits.ZB) == (bunits.YB / 1024 ** 7, 'ZiB')

    def test_yobibyte(self):
        assert convert_units(1, bunits.YB, bunits.YB) == (bunits.YB / 1024 ** 8, 'YiB')

    def test_kilobyte(self):
        assert convert_units(1, dunits.YB, dunits.KB) == (dunits.YB / 1000 ** 1, 'KB')

    def test_megabyte(self):
        assert convert_units(1, dunits.YB, dunits.MB) == (dunits.YB / 1000 ** 2, 'MB')

    def test_gigabyte(self):
        assert convert_units(1, dunits.YB, dunits.GB) == (dunits.YB / 1000 ** 3, 'GB')

    def test_terabyte(self):
        assert convert_units(1, dunits.YB, dunits.TB) == (dunits.YB / 1000 ** 4, 'TB')

    def test_petabyte(self):
        assert convert_units(1, dunits.YB, dunits.PB) == (dunits.YB / 1000 ** 5, 'PB')

    def test_exabyte(self):
        assert convert_units(1, dunits.YB, dunits.EB) == (dunits.YB / 1000 ** 6, 'EB')

    def test_zettabyte(self):
        assert convert_units(1, dunits.YB, dunits.ZB) == (dunits.YB / 1000 ** 7, 'ZB')

    def test_yottabyte(self):
        assert convert_units(1, dunits.YB, dunits.YB) == (dunits.YB / 1000 ** 8, 'YB')


class TestConvertUnknownTo:
    def test_byte(self):
        assert convert_units(bunits.B) == (bunits.B, 'B')
        assert convert_units(bunits.KB - 1) == (bunits.KB - 1, 'B')
        assert convert_units(dunits.B, si=True) == (dunits.B, 'B')
        assert convert_units(dunits.KB - 1, si=True) == (dunits.KB - 1, 'B')

    def test_kibibyte(self):
        assert convert_units(bunits.KB) == (bunits.KB / bunits.KB, 'KiB')
        assert convert_units(bunits.MB - 1) == ((bunits.MB - 1) / bunits.KB, 'KiB')

    def test_mebibyte(self):
        assert convert_units(bunits.MB) == (bunits.MB / bunits.MB, 'MiB')
        assert convert_units(bunits.GB - 1) == ((bunits.GB - 1) / bunits.MB, 'MiB')

    def test_gibibyte(self):
        assert convert_units(bunits.GB) == (bunits.GB / bunits.GB, 'GiB')
        assert convert_units(bunits.TB - 1) == ((bunits.TB - 1) / bunits.GB, 'GiB')

    def test_tebibyte(self):
        assert convert_units(bunits.TB) == (bunits.TB / bunits.TB, 'TiB')
        assert convert_units(bunits.PB - 1) == ((bunits.PB - 1) / bunits.TB, 'TiB')

    def test_pebibyte(self):
        assert convert_units(bunits.PB) == (bunits.PB / bunits.PB, 'PiB')
        assert convert_units(bunits.EB - 1) == ((bunits.EB - 1) / bunits.PB, 'PiB')

    def test_exbibyte(self):
        assert convert_units(bunits.EB) == (bunits.EB / bunits.EB, 'EiB')
        assert convert_units(bunits.ZB - 1) == ((bunits.ZB - 1) / bunits.EB, 'EiB')

    def test_zebibyte(self):
        assert convert_units(bunits.ZB) == (bunits.ZB / bunits.ZB, 'ZiB')
        assert convert_units(bunits.YB - 1) == ((bunits.YB - 1) / bunits.ZB, 'ZiB')

    def test_yobibyte(self):
        assert convert_units(bunits.YB) == (bunits.YB / bunits.YB, 'YiB')

    def test_kilobyte(self):
        assert convert_units(dunits.KB, si=True) == (dunits.KB / dunits.KB, 'KB')
        assert convert_units(dunits.MB - 1, si=True) == ((dunits.MB - 1) / dunits.KB, 'KB')

    def test_megabyte(self):
        assert convert_units(dunits.MB, si=True) == (dunits.MB / dunits.MB, 'MB')
        assert convert_units(dunits.GB - 1, si=True) == ((dunits.GB - 1) / dunits.MB, 'MB')

    def test_gigabyte(self):
        assert convert_units(dunits.GB, si=True) == (dunits.GB / dunits.GB, 'GB')
        assert convert_units(dunits.TB - 1, si=True) == ((dunits.TB - 1) / dunits.GB, 'GB')

    def test_terabyte(self):
        assert convert_units(dunits.TB, si=True) == (dunits.TB / dunits.TB, 'TB')
        assert convert_units(dunits.PB - 1, si=True) == ((dunits.PB - 1) / dunits.TB, 'TB')

    def test_petabyte(self):
        assert convert_units(dunits.PB, si=True) == (dunits.PB / dunits.PB, 'PB')
        assert convert_units(dunits.EB - 1, si=True) == ((dunits.EB - 1) / dunits.PB, 'PB')

    def test_exabyte(self):
        assert convert_units(dunits.EB, si=True) == (dunits.EB / dunits.EB, 'EB')
        assert convert_units(dunits.ZB - 1, si=True) == ((dunits.ZB - 1) / dunits.EB, 'EB')

    def test_zettabyte(self):
        assert convert_units(dunits.ZB, si=True) == (dunits.ZB / dunits.ZB, 'ZB')
        assert convert_units(dunits.YB - 1, si=True) == ((dunits.YB - 1) / dunits.ZB, 'ZB')

    def test_yottabyte(self):
        assert convert_units(dunits.YB, si=True) == (dunits.YB / dunits.YB, 'YB')


class TestUnknownUnits:
    def test_unit(self):
        with pytest.raises(ValueError):
            convert_units(1, unit=5)

    def test_to(self):
        with pytest.raises(ValueError):
            convert_units(1, to=5)
