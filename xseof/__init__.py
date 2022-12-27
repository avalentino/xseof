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


__version__ = "1.1.1.dev0"
_modules = (
    aux_orbdop,
    aux_orbdor,
    aux_orbres,
    int_attref,
    mpl_orbpre,
    mpl_orbref,
)


def _is_xmldoc(source):
    return hasattr(source, "getroot") or hasattr(source, "tag")


def _fix_namespaces(source: Union[str, bytes]) -> Union[str, bytes]:
    from lxml import etree

    if isinstance(source, (str, bytes)):
        root = etree.fromstring(source)
    else:
        root = source if not hasattr(source, "getroot") else source.getroot()

    root_tags = {"Earth_Explorer_File", "Earth_Observation_File"}

    if root.tag not in root_tags or root.nsmap:
        if isinstance(source, str):
            source = source.encode("utf-8")
        return source

    nsmap = {
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        None: "http://eop-cfi.esa.int/CFI",
    }
    new_root = etree.Element(root.tag, attrib=root.attrib, nsmap=nsmap)
    new_root[:] = root[:]
    new_xml = etree.ElementTree(new_root)

    return etree.tostring(new_xml, pretty_print=True, xml_declaration=True)


def _safe_fix_namespaces(source: Union[str, bytes]) -> Union[str, bytes]:
    try:
        fixed_source = _fix_namespaces(source)
    except (ImportError, SyntaxError):
        fixed_source = source

    if isinstance(fixed_source, str):
        fixed_source = fixed_source.encode("utf-8")

    return fixed_source


def from_string(source: Union[str, bytes], strict: bool = False):
    """Load on EOF onject from the source string or bytes string.

    The `strict` parameter (default: `False`) enforces stricy checking
    of XML namespaces.
    """
    parser = XmlParser()

    if isinstance(source, str):
        parse = parser.from_string
    else:
        parse = parser.from_bytes

    try:
        return parse(source)
    except ParserError:
        if not strict:
            source = _safe_fix_namespaces(source)
            try:
                return parser.from_bytes(source)
            except ParserError:
                pass
        for mod in _modules:
            try:
                return mod.from_string(source)
            except ParserError:
                pass
        raise


def load(source, strict: bool = False):
    """Load an EOF object from the source stream.

    The input stream can be a filename, a file like object (open in
    binary mode) or an xml ElementTree (lxml is needed for the latter).

    The `strict` parameter (default: `False`) enforces stricy checking
    of XML namespaces.
    """
    if hasattr(source, "tell"):
        data = source.read()
        return from_string(data, strict=strict)
    else:
        parser = XmlParser()
        try:
            return parser.parse(source)
        except ParserError:
            if _is_xmldoc(source):
                # xml object to bytes
                source = _safe_fix_namespaces(source)
            else:
                # assume it is a file path
                with open(source, "rb") as fd:
                    source = fd.read()
            return from_string(source, strict=strict)
