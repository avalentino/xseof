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
from xsdata.formats.dataclass.parsers import XmlParser

from . import aux_orbdop  # noqa: F401
from . import aux_orbdor  # noqa: F401
from . import aux_orbres  # noqa: F401
from . import int_attref  # noqa: F401
from . import mpl_orbpre  # noqa: F401
from . import mpl_orbref  # noqa: F401


__version__ = "1.0.0"


def _fix_namespaces(source: Union[str, bytes]) -> Union[str, bytes]:
    from lxml import etree

    root_tags = {"Earth_Explorer_File", "Earth_Observation_File"}

    root = etree.fromstring(source)
    if root.tag not in root_tags or root.nsmap:
        raise ValueError()

    nsmap = {
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        None: "http://eop-cfi.esa.int/CFI",
    }
    root2 = etree.Element(root.tag, attrib=root.attrib, nsmap=nsmap)
    root2[:] = root[:]
    xml2 = etree.ElementTree(root2)

    return etree.tostring(xml2, pretty_print=True, xml_declaration=True)


def from_string(source: Union[str, bytes]):
    """Load on EOF onject from the source string or bytes string."""
    parser = XmlParser()

    if isinstance(source, str):
        parse = parser.from_string
    else:
        parse = parser.from_bytes

    try:
        return parse(source)
    except ParserError:
        try:
            source = _fix_namespaces(source)
            return parse(source)
        except (ImportError, SyntaxError):
            pass
        raise


def load(source):
    """Load an EOF object from the source stream.

    The input stream can be a filename, a file like object (open in
    binary mode) or an xml ElementTree.
    """
    if hasattr(source, "tell"):
        data = source.read()
        return from_string(data)
    else:
        try:
            parser = XmlParser()
            return parser.parse(source)
        except ParserError:
            with open(source, "rb") as fd:
                source = fd.read()
            return from_string(source)
