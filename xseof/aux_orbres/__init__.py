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
from .eo_oper_aux_orbres_0203 import (  # noqa: F401
    EarthExplorerFile as AuxOrbResFileV0203,
)
from .eo_oper_aux_orbres_0300 import (  # noqa: F401
    EarthObservationFile as AuxOrbResFileV0300,
)


_type_name = "AuxOrbResFile"
_type_description = __doc__.rstrip(".")
_type_classes = tuple(
    clazz for name, clazz in sorted(globals().items(), reverse=True)
    if name.startswith(_type_name)
)


def from_string(source: Union[str, bytes]):
    """Load a Restituted Orbit from the source string or bytes string."""
    parser = XmlParser()

    if isinstance(source, str):
        parse = parser.from_string
    else:
        parse = parser.from_bytes

    for clazz in _type_classes:
        try:
            return parse(source, clazz)
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to load {_type_description}")


def load(source):
    """Load a Restituted Orbit from the source stream.

    The input stream can be a filename, a file like object (open in
    binary mode) or an xml ElementTree (lxml is needed for the latter).
    """
    if hasattr(source, "read"):
        return from_string(source.read())

    parser = XmlParser()
    for clazz in _type_classes:
        try:
            return parser.parse(source, clazz)
        except ParserError:
            pass
    else:
        raise ParserError(
            f"Unable to load DORIS {_type_description} form {source}")
