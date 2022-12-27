"""I/O library for the ESA EOF files.

This package provides a set of "dataclasses", comapible with the xsdata_
Python library, to access and make I/O operation on the XML files in the
ESA Earth Observation Ground Segment File Format (EOF).

In particular, this package support all the XML based orbit and attitude
products.

.. _xsdata: https://github.com/tefra/xsdata
"""

import io
import copy
from typing import Union
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser

from . import aux_orbdop
from . import aux_orbdor
from . import aux_orbres
from . import int_attref
from . import mpl_orbpre
from . import mpl_orbref


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


def _fix_namespaces(source):
    from lxml import etree

    if isinstance(source, str):
        xmldoc = etree.parse(io.StringIO(source))
    elif isinstance(source, bytes):
        xmldoc = etree.parse(io.BytesIO(source))
    elif _is_xmldoc(source):
        # is an xml object
        xmldoc = (
            etree.ElementTree(source) if hasattr(source, "tag") else source
        )
    else:
        raise TypeError(f"invalid 'source' type: {type(source)!r}")

    root_tags = {"Earth_Explorer_File", "Earth_Observation_File"}

    root = xmldoc.getroot()
    if root.tag not in root_tags or root.nsmap:
        return xmldoc

    nsmap = {
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        None: "http://eop-cfi.esa.int/CFI",
    }
    new_root = etree.Element(root.tag, attrib=root.attrib, nsmap=nsmap)
    new_root[:] = root[:]
    new_xmldoc = etree.ElementTree(new_root)

    return new_xmldoc


def _safe_fix_namespaces(source) -> bytes:
    try:
        from lxml import etree
        xmldoc = _fix_namespaces(source)
        fixed_source = etree.tostring(
            xmldoc, pretty_print=True, xml_declaration=True
        )
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
    elif isinstance(source, bytes):
        parse = parser.from_bytes
    else:
        raise ValueError(
            f"invalid 'source' type ({type(source)!r}), str or bytes expected"
        )

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


def _from_xml(source, strict: bool = False):
    assert _is_xmldoc(source)

    xmldoc = source
    source = copy.deepcopy(xmldoc)

    parser = XmlParser()
    try:
        return parser.parse(source)
    except ParserError:
        if strict:
            for mod in _modules:
                # see https://github.com/tefra/xsdata/issues/683
                source = copy.deepcopy(xmldoc)
                try:
                    return mod._from_xml(source)
                except ParserError:
                    pass
            raise
        else:
            # xml object to bytes
            source = _safe_fix_namespaces(xmldoc)
            return from_string(source, strict=strict)


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
    elif _is_xmldoc(source):
        return _from_xml(source, strict)
    else:
        parser = XmlParser()
        try:
            return parser.parse(source)
        except ParserError:
            # assume it is a file path
            with open(source, "rb") as fd:
                source = fd.read()
            return from_string(source, strict=strict)
