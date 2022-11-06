"""Predicted Orbit File."""

from typing import Union 
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser


_type_name = "PredictedOrbitFileType"
_type_description = __doc__.rstrip(".")


def parse(source):
    from . import v01xx, v02xx, v03xx

    parser = XmlParser()

    for pkg in v03xx, v02xx, v01xx:
        try:
            return parser.parse(source, getattr(pkg, _type_name))
        except ParserError:
            pass
    else:
        raise ParserError(
            f"Unable to load DORIS {_type_description} form {source}")


def from_string(source: Union[str, bytes]):
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
