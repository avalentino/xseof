"""I/O library for the ESA EOF files.

This package provides a set of "dataclasses", comapible with the xsdata_
Python library, to access and make I/O operation on the XML files in the
ESA Earth Observation Ground Segment File Format (EOF).

In particular, this package support all the XML based orbit and attitude
products.

.. _xsdata: https://github.com/tefra/xsdata
"""


from typing import Union
from xsdata.exceptions import ParserError

import xseof.aux_orbdop
import xseof.aux_orbdor
import xseof.aux_orbres
import xseof.int_attref
import xseof.mpl_orbpre
import xseof.mpl_orbref


__version__ = "1.0.0.dev0"


def load(source):
    """Load an EOF object from the source stream.

    The input stream can be a filename, a file like object (open in
    binary mode) or an xml ElementTree.
    """
    for mod in (xseof.aux_orbdop, xseof.aux_orbdor, xseof.aux_orbres,
                xseof.int_attref, xseof.mpl_orbpre, xseof.mpl_orbref):
        try:
            return mod.load(source)
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to parse {source}")


def from_string(source: Union[str, bytes]):
    """Load on EOF onject from the source string or bytes string."""
    for mod in (xseof.aux_orbdop, xseof.aux_orbdor, xseof.aux_orbres,
                xseof.int_attref, xseof.mpl_orbpre, xseof.mpl_orbref):
        try:
            return mod.from_string(source)
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to parse {source}")
