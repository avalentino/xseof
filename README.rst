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

