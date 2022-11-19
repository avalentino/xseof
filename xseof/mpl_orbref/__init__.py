"""Reference Orbit Event File."""

from typing import Union
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser

from .eo_oper_mpl_orbref_0100 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0100,
)
from .eo_oper_mpl_orbref_0101 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0101,
)
from .eo_oper_mpl_orbref_0102 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0102,
)
from .eo_oper_mpl_orbref_0103 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0103,
)
from .eo_oper_mpl_orbref_0104 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0104,
)
from .eo_oper_mpl_orbref_0105 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0105,
)
from .eo_oper_mpl_orbref_0106 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0106,
)
from .eo_oper_mpl_orbref_0200 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0200,
)
from .eo_oper_mpl_orbref_0201 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0201,
)
from .eo_oper_mpl_orbref_0202 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0202,
)
from .eo_oper_mpl_orbref_0300 import (  # noqa: F401
    EarthObservationFile as MplOrbRefFileV0300,
)

_type_name = "MplOrbRefFile"
_type_description = __doc__.rstrip(".")


def load(source):
    """Load a Reference Orbit Event from the source stream.

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
    """Load a Reference Orbit Event from the source string or bytes string."""
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
