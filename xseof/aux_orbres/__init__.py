"""Restituted Orbit File."""

from typing import Union
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser

from .eo_oper_aux_orbres_0100 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0100,
)
from .eo_oper_aux_orbres_0101 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0101,
)
from .eo_oper_aux_orbres_0102 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0102,
)
from .eo_oper_aux_orbres_0103 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0103,
)
from .eo_oper_aux_orbres_0104 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0104,
)
from .eo_oper_aux_orbres_0105 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0105,
)
from .eo_oper_aux_orbres_0200 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0200,
)
from .eo_oper_aux_orbres_0201 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0201,
)
from .eo_oper_aux_orbres_0202 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0202,
)
from .eo_oper_aux_orbres_0300 import (  # noqa: F401
    EarthObservationFile as AuxOrbResFileV0300,
)


_type_name = "AuxOrbResFile"
_type_description = __doc__.rstrip(".")


def load(source):
    """Load a Restituted Orbit from the source stream.

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
    """Load a Restituted Orbit from the source string or bytes string."""
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
