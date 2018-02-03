binary
======

.. image:: https://img.shields.io/pypi/v/binary.svg?style=flat-square
    :target: https://pypi.org/project/binary
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/ofek/binary/master.svg?style=flat-square
    :target: https://travis-ci.org/ofek/binary
    :alt: Travis CI

.. image:: https://img.shields.io/appveyor/ci/ofek/binary/master.svg?style=flat-square
    :target: https://ci.appveyor.com/project/ofek/binary
    :alt: AppVeyor CI

.. image:: https://img.shields.io/codecov/c/github/ofek/binary/master.svg?style=flat-square
    :target: https://codecov.io/gh/ofek/binary
    :alt: Codecov

.. image:: https://img.shields.io/pypi/pyversions/binary.svg?style=flat-square
    :target: https://pypi.org/project/binary
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/l/binary.svg?style=flat-square
    :target: https://choosealicense.com/licenses
    :alt: License

-----

``binary`` provides a bug-free and easy way to convert between and within
binary (`IEC`_) and decimal (`SI`_) units.

.. contents:: **Table of Contents**
    :backlinks: none

Installation
------------

``binary`` is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 2.7/3.5+ and PyPy.

.. code-block:: bash

    $ pip install binary

Examples
--------

Let's import what we need:

.. code-block:: python

    >>> from binary import BinaryUnits, DecimalUnits, convert_units

**Basic conversion:**

.. code-block:: python

    >>> convert_units(1536, BinaryUnits.KB, BinaryUnits.MB)
    (1.5, 'MiB')

**How much actual storage your new hard drive has:**

.. code-block:: python

    >>> convert_units(4, DecimalUnits.TB, BinaryUnits.TB)
    (3.637978807091713, 'TiB')

**Human readable:**

.. code-block:: python

    >>> amount, unit = convert_units(kubernetes_ingest_bytes_per_second)
    >>> 'Incoming traffic: {:.2f} {}/s'.format(amount, unit)
    'Incoming traffic: 24.77 GiB/s'

Usage
-----

Just a single function!

``convert_units(n, unit=BYTE, to=None, si=False, exact=False)``

Converts between and within binary and decimal units. If no ``unit``
is specified, ``n`` is assumed to already be in bytes. If no ``to`` is
specified, ``n`` will be converted to the highest unit possible. If
no ``unit`` nor ``to`` is specified, the output will be binary units
unless ``si`` is ``True``. If ``exact`` is ``True``. the calculations
will use ``decimal.Decimal``.

| Binary units conform to IEC standards, see:
| `<https://en.wikipedia.org/wiki/Binary_prefix>`_
| `<https://en.wikipedia.org/wiki/IEC_80000-13>`_
| `<https://www.iso.org/standard/31898.html>`_ (paywalled)
|
| Decimal units conform to SI standards, see:
| `<https://en.wikipedia.org/wiki/International_System_of_Units>`_
|

* Parameters

  - **n** (``int`` or ``float``) - The number of ``unit``\ s.
  - **unit** - The unit ``n`` represents. See `types`_.
  - **to** - The unit to convert to. See `types`_.
  - **si** (``bool``) - Assume SI units when no ``unit`` nor ``to`` is specified.
  - **exact** (``bool``) - Use ``decimal.Decimal`` for calculations.

Types
^^^^^

Although the string representations for binary units end in ``iB``,
the attributes do not for ease of use.

+--------------+-------+-----------+
| Type         | Short | Long      |
+==============+=======+===========+
| BinaryUnits  | B     | BYTE      |
+--------------+-------+-----------+
| BinaryUnits  | KB    | KIBIBYTE  |
+--------------+-------+-----------+
| BinaryUnits  | MB    | MEBIBYTE  |
+--------------+-------+-----------+
| BinaryUnits  | GB    | GIBIBYTE  |
+--------------+-------+-----------+
| BinaryUnits  | TB    | TEBIBYTE  |
+--------------+-------+-----------+
| BinaryUnits  | PB    | PEBIBYTE  |
+--------------+-------+-----------+
| BinaryUnits  | EB    | EXBIBYTE  |
+--------------+-------+-----------+
| BinaryUnits  | ZB    | ZEBIBYTE  |
+--------------+-------+-----------+
| BinaryUnits  | YB    | YOBIBYTE  |
+--------------+-------+-----------+
| DecimalUnits | B     | BYTE      |
+--------------+-------+-----------+
| DecimalUnits | KB    | KILOBYTE  |
+--------------+-------+-----------+
| DecimalUnits | MB    | MEGABYTE  |
+--------------+-------+-----------+
| DecimalUnits | GB    | GIGABYTE  |
+--------------+-------+-----------+
| DecimalUnits | TB    | TERABYTE  |
+--------------+-------+-----------+
| DecimalUnits | PB    | PETABYTE  |
+--------------+-------+-----------+
| DecimalUnits | EB    | EXABYTE   |
+--------------+-------+-----------+
| DecimalUnits | ZB    | ZETTABYTE |
+--------------+-------+-----------+
| DecimalUnits | YB    | YOTTABYTE |
+--------------+-------+-----------+

License
-------

``binary`` is distributed under the terms of both

- `MIT License <https://choosealicense.com/licenses/mit>`_
- `Apache License, Version 2.0 <https://choosealicense.com/licenses/apache-2.0>`_

at your option.

Changelog
---------

Important changes are emphasized.

1.0.0
^^^^^

- Initial release

.. _IEC: https://en.wikipedia.org/wiki/Binary_prefix
.. _SI: https://en.wikipedia.org/wiki/International_System_of_Units
