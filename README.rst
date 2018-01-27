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

License
-------

``binary`` is distributed under the terms of both

- `MIT License <https://choosealicense.com/licenses/mit>`_
- `Apache License, Version 2.0 <https://choosealicense.com/licenses/apache-2.0>`_

at your option.

.. _IEC: https://en.wikipedia.org/wiki/Binary_prefix
.. _SI: https://en.wikipedia.org/wiki/International_System_of_Units
