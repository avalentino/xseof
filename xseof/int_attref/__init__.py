"""Attitude File."""

from typing import Union
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser

from .eo_oper_int_attref_0101 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0101,
)
from .eo_oper_int_attref_0102 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0102,
)
from .eo_oper_int_attref_0103 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0103,
)
from .eo_oper_int_attref_0104 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0104,
)
from .eo_oper_int_attref_0200 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0200,
)
from .eo_oper_int_attref_0201 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0201,
)
from .eo_oper_int_attref_0202 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0202,
)
from .eo_oper_int_attref_0203 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0203,
)
from .eo_oper_int_attref_0204 import (  # noqa: F401
    EarthExplorerFile as IntAttRefFileV0204,
)
from .eo_oper_int_attref_0300 import (  # noqa: F401
    EarthObservationFile as IntAttRefFileV0300,
)
from .eo_oper_int_attref_0301 import (  # noqa: F401
    EarthObservationFile as IntAttRefFileV0301,
)

_type_name = "IntAttRefFile"
_type_description = __doc__.rstrip(".")


def load(source):
    """Load the Attitude from the source stream.

    The input stream can be a filename, a file like object (open in
    binary mode) or an xml ElementTree.
    """
    parser = XmlParser()

    pos = source.tell() if hasattr(source, "tell") else None

    classes = [
        clazz for name, clazz in globals().items()
        if name.startswith(_type_name)
    ]

    for clazz in classes:
        try:
            if pos is not None:
                source.seek(pos)
            return parser.parse(source, clazz)
        except ParserError:
            pass
    else:
        raise ParserError(
            f"Unable to load DORIS {_type_description} form {source}")


def from_string(source: Union[str, bytes]):
    """Load the Attitude from the source string or bytes string."""
    parser = XmlParser()

    if isinstance(source, str):
        parse = parser.from_string
    else:
        parse = parser.from_bytes

    classes = [
        clazz for name, clazz in globals().items()
        if name.startswith(_type_name)
    ]

    for clazz in classes:
        try:
            return parse(source, clazz)
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to load {_type_description}")
