"""I/O library for the ESA EOF files.

This package provides a set of "dataclasses", comapible with the xsdata_
Python library, to access and make I/O operation on the XML files in the
ESA Earth Observation Ground Segment File Format (EOF).

In particular, this package support all the XML based orbit and attitude
products.

.. _xsdata: https://github.com/tefra/xsdata
"""


from typing import Union 
from xsdata.formats.dataclass.parsers import XmlParser


__version__ = "1.0.0.dev0"


def _import_all():
    """Lazy import modules for all the products types and all versions."""
    import xseof.aux_orbdop.v01xx
    import xseof.aux_orbdop.v02xx
    import xseof.aux_orbdop.v03xx

    import xseof.aux_orbdor.v01xx
    import xseof.aux_orbdor.v02xx
    import xseof.aux_orbdor.v03xx

    import xseof.aux_orbres.v01xx
    import xseof.aux_orbres.v02xx
    import xseof.aux_orbres.v03xx

    import xseof.int_attref.v01xx
    import xseof.int_attref.v02xx
    import xseof.int_attref.v03xx

    import xseof.mpl_orbpre.v01xx
    import xseof.mpl_orbpre.v02xx
    import xseof.mpl_orbpre.v03xx

    import xseof.mpl_orbref.v01xx
    import xseof.mpl_orbref.v02xx
    import xseof.mpl_orbref.v03xx


def parse(source):
    _import_all()

    parser = XmlParser()

    return parser.parse(source)


def from_string(source: Union[str, bytes]):
    _import_all()

    parser = XmlParser()

    if isinstance(source, str):
        parse = parser.from_string
    else:
        parse = parser.from_bytes

    return parse(source)
