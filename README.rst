xseof
=====

Overview
--------

I/O library for the ESA EOF files.

This package provides a set of "dataclasses", comapible with the
xsdata_ Python library, to access and make I/O operation on the XML files
in the ESA Earth Observation Ground Segment File Format (EOF) [1]_.

In particular, this package supports all the XML based orbit and attitude
products described in [1]_.


Project links
-------------

:Home Page:
    https://github.com/avalentino/xseof
:Download:
    https://pypi.org/project/xseof


Installation
------------

Standard installation via pip_::

    $ pip install xseof


Testing
-------

Move to the the source directory root and run the following command::

    $ python3 -m pytest


Basic usage
-----------

Load a generic orbit file::

    >>> import xseof
    >>> orbit = xseof.load(
            "MA1_TEST_AUX_ORBRES_20210610T045753_20210610T065853_0001.EOF")


Access and print loaded data::

    >>> import pprint
    >>> orbit.earth_observation_header.fixed_header.notes = ""
    >>> pprint.pprint(orbit.earth_observation_header.fixed_header)
    FixedHeaderType(
        file_name='MA1_TEST_AUX_ORBRES_20210610T045753_20210610T065853_0001',
        file_description='FOS Orbit File',
        notes='',
        mission='MetOpSGA1',
        file_class='TEST',
        file_type='AUX_ORBRES',
        validity_period=ValidityPeriodType(
            validity_start='UTC=2021-06-10T04:57:53',
            validity_stop='UTC=2021-06-10T05:02:23'),
        file_version='0001',
        eoffs_version='3.0',
        source=SourceType(system='System Identification as per Ground '
                                'Segment File Format Standard '
                                '(PE-TN-ESA-GS-0001)',
                        creator='Creator Identification as per '
                                'Ground Segment File Format Standard '
                                '(PE-TN-ESA-GS-0001)',
                        creator_version='Creator Version '
                                        'Identification as per '
                                        'Ground Segment File Format '
                                        'Standard '
                                        '(PE-TN-ESA-GS-0001)',
                        creation_date='UTC=2022-06-23T10:06:43'))

    >>> print(orbit.data_block.list_of_osvs.count)
    10
    >>> pprint.pprint(orbit.data_block.list_of_osvs.osv[0])
    OsvType(tai='TAI=2021-06-10T04:57:17.817060',
        utc='UTC=2021-06-10T04:57:52.817060',
        ut1='UT1=2021-06-10T04:57:53.117059',
        absolute_orbit=999,
        x=PositionComponentType(value=Decimal('-1606749.988'), unit='m'),
        y=PositionComponentType(value=Decimal('-5677008.966'), unit='m'),
        z=PositionComponentType(value=Decimal('-4135675.595'), unit='m'),
        vx=VelocityComponentType(value=Decimal('-2876.652288'), unit='m/s'),
        vy=VelocityComponentType(value=Decimal('-3541.028256'), unit='m/s'),
        vz=VelocityComponentType(value=Decimal('5985.303441'), unit='m/s'),
        quality='0000000000000')


Load an EOF file of a specific type::

    >>> from xseof import int_attref
    >>> quaternions = int_attref.load(
            "MA1_TEST_INT_ATTREF_20210610T045753_20210610T065853_0001.EOF")


Load data form string::

    >>> from xseof import aux_orbres
    >>> filename = "MA1_TEST_AUX_ORBRES_20210610T045753_20210610T065853_0001.EOF"
    >>> with open(filename) as fd:
    ...     data = fd.read()
    >>> orbit = aux_orbres.from_string(data)


Licanse
-------

Copyright 2022 Antonio Valentino

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific langua


.. _xsdata: https://github.com/tefra/xsdata
.. _pip: https://pip.pypa.io

.. [1] https://eop-cfi.esa.int/Repo/PUBLIC/DOCUMENTATION/SYSTEM_SUPPORT_DOCS/PE-TN-ESA-GS-0001%20EO%20GS%20File%20Format%20Standard%203.0%20signed.pdf

