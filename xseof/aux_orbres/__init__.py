"""Restituted Orbit File."""

from typing import Union
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser


_type_name = "RestitutedOrbitFileType"
_type_description = __doc__.rstrip(".")


def load(source):
    """Load a Restituted Orbit from the source stream.

    The input stream can be a filename, a file like object (open in
    binary mode) or an xml ElementTree.
    """
    from . import v01xx, v02xx, v03xx

    parser = XmlParser()

    pos = source.tell() if hasattr(source, "tell") else None

    for pkg in v03xx, v02xx, v01xx:
        try:
            if pos is not None:
                source.seek(pos)
            return parser.parse(source, getattr(pkg, _type_name))
        except ParserError as exc:
            pass
    else:
        raise ParserError(
            f"Unable to load DORIS {_type_description} form {source}")


def from_string(source: Union[str, bytes]):
    """Load a Restituted Orbit from the source string or bytes string."""
    from . import v01xx, v02xx, v03xx

    parser = XmlParser()

    if isinstance(source, str):
        parse = parser.from_string
    else:
        parse = parser.from_bytes

    for pkg in v03xx, v02xx, v01xx:
        try:
            return parse(source, getattr(pkg, _type_name))
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to load {_type_description}")
