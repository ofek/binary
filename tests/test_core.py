from __future__ import division

import pytest

import binary
from binary.core import BINARY_PREFIX


class TestConstants:
    def test_byte(self):
        assert binary.BYTE == binary.B == 1024 ** 0

    def test_kibibyte(self):
        assert binary.KIBIBYTE == binary.KB == 1024 ** 1

    def test_mebibyte(self):
        assert binary.MEBIBYTE == binary.MB == 1024 ** 2

    def test_gibibyte(self):
        assert binary.GIBIBYTE == binary.GB == 1024 ** 3

    def test_tebibyte(self):
        assert binary.TEBIBYTE == binary.TB == 1024 ** 4

    def test_pebibyte(self):
        assert binary.PEBIBYTE == binary.PB == 1024 ** 5

    def test_exbibyte(self):
        assert binary.EXBIBYTE == binary.EB == 1024 ** 6

    def test_zebibyte(self):
        assert binary.ZEBIBYTE == binary.ZB == 1024 ** 7

    def test_yobibyte(self):
        assert binary.YOBIBYTE == binary.YB == 1024 ** 8


class TestAccurateString:
    def test_byte(self):
        assert BINARY_PREFIX[binary.BYTE] == 'B'

    def test_kibibyte(self):
        assert BINARY_PREFIX[binary.KIBIBYTE] == 'KiB'

    def test_mebibyte(self):
        assert BINARY_PREFIX[binary.MEBIBYTE] == 'MiB'

    def test_gibibyte(self):
        assert BINARY_PREFIX[binary.GIBIBYTE] == 'GiB'

    def test_tebibyte(self):
        assert BINARY_PREFIX[binary.TEBIBYTE] == 'TiB'

    def test_pebibyte(self):
        assert BINARY_PREFIX[binary.PEBIBYTE] == 'PiB'

    def test_exbibyte(self):
        assert BINARY_PREFIX[binary.EXBIBYTE] == 'EiB'

    def test_zebibyte(self):
        assert BINARY_PREFIX[binary.ZEBIBYTE] == 'ZiB'

    def test_yobibyte(self):
        assert BINARY_PREFIX[binary.YOBIBYTE] == 'YiB'


class TestConvert:
    def test_byte(self):
        assert binary.convert_units(1, binary.YB, binary.B) == (binary.YB / 1024 ** 0, 'B')

    def test_kibibyte(self):
        assert binary.convert_units(1, binary.YB, binary.KB) == (binary.YB / 1024 ** 1, 'KiB')

    def test_mebibyte(self):
        assert binary.convert_units(1, binary.YB, binary.MB) == (binary.YB / 1024 ** 2, 'MiB')

    def test_gibibyte(self):
        assert binary.convert_units(1, binary.YB, binary.GB) == (binary.YB / 1024 ** 3, 'GiB')

    def test_tebibyte(self):
        assert binary.convert_units(1, binary.YB, binary.TB) == (binary.YB / 1024 ** 4, 'TiB')

    def test_pebibyte(self):
        assert binary.convert_units(1, binary.YB, binary.PB) == (binary.YB / 1024 ** 5, 'PiB')

    def test_exbibyte(self):
        assert binary.convert_units(1, binary.YB, binary.EB) == (binary.YB / 1024 ** 6, 'EiB')

    def test_zebibyte(self):
        assert binary.convert_units(1, binary.YB, binary.ZB) == (binary.YB / 1024 ** 7, 'ZiB')

    def test_yobibyte(self):
        assert binary.convert_units(1, binary.YB, binary.YB) == (binary.YB / 1024 ** 8, 'YiB')


class TestConvertUnknownTo:
    def test_byte(self):
        assert binary.convert_units(binary.B) == (binary.B, 'B')
        assert binary.convert_units(binary.KB - 1) == (binary.KB - 1, 'B')

    def test_kibibyte(self):
        assert binary.convert_units(binary.KB) == (binary.KB / binary.KB, 'KiB')
        assert binary.convert_units(binary.MB - 1) == ((binary.MB - 1) / binary.KB, 'KiB')

    def test_mebibyte(self):
        assert binary.convert_units(binary.MB) == (binary.MB / binary.MB, 'MiB')
        assert binary.convert_units(binary.GB - 1) == ((binary.GB - 1) / binary.MB, 'MiB')

    def test_gibibyte(self):
        assert binary.convert_units(binary.GB) == (binary.GB / binary.GB, 'GiB')
        assert binary.convert_units(binary.TB - 1) == ((binary.TB - 1) / binary.GB, 'GiB')

    def test_tebibyte(self):
        assert binary.convert_units(binary.TB) == (binary.TB / binary.TB, 'TiB')
        assert binary.convert_units(binary.PB - 1) == ((binary.PB - 1) / binary.TB, 'TiB')

    def test_pebibyte(self):
        assert binary.convert_units(binary.PB) == (binary.PB / binary.PB, 'PiB')
        assert binary.convert_units(binary.EB - 1) == ((binary.EB - 1) / binary.PB, 'PiB')

    def test_exbibyte(self):
        assert binary.convert_units(binary.EB) == (binary.EB / binary.EB, 'EiB')
        assert binary.convert_units(binary.ZB - 1) == ((binary.ZB - 1) / binary.EB, 'EiB')

    def test_zebibyte(self):
        assert binary.convert_units(binary.ZB) == (binary.ZB / binary.ZB, 'ZiB')
        assert binary.convert_units(binary.YB - 1) == ((binary.YB - 1) / binary.ZB, 'ZiB')

    def test_yobibyte(self):
        assert binary.convert_units(binary.YB) == (binary.YB / binary.YB, 'YiB')


class TestUnknownUnits:
    def test_unit(self):
        with pytest.raises(ValueError):
            binary.convert_units(1, unit=1000)

    def test_to(self):
        with pytest.raises(ValueError):
            binary.convert_units(1, to=1000)
