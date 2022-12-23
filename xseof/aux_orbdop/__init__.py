"""DORIS Preliminary Orbit File."""

from typing import Union
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser

from .eo_oper_aux_orbdop_0100 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0100,
)
from .eo_oper_aux_orbdop_0101 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0101,
)
from .eo_oper_aux_orbdop_0102 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0102,
)
from .eo_oper_aux_orbdop_0103 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0103,
)
from .eo_oper_aux_orbdop_0104 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0104,
)
from .eo_oper_aux_orbdop_0105 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0105,
)
from .eo_oper_aux_orbdop_0200 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0200,
)
from .eo_oper_aux_orbdop_0201 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0201,
)
from .eo_oper_aux_orbdop_0202 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0202,
)
from .eo_oper_aux_orbdop_0203 import (  # noqa: F401
    EarthExplorerFile as AuxOrbDopFileV0203,
)
from .eo_oper_aux_orbdop_0300 import (  # noqa: F401
    EarthObservationFile as AuxOrbDopFileV0300,
)


_type_name = "AuxOrbDopFile"
_type_description = __doc__.rstrip(".")
_type_classes = tuple(
    clazz for name, clazz in sorted(globals().items(), reverse=True)
    if name.startswith(_type_name)
)


def from_string(source: Union[str, bytes]):
    """Load DORIS Preliminary Orbit from the source string or bytes string."""
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
    """Load a DORIS Preliminary Orbit from the source stream.

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
