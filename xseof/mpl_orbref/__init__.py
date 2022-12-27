"""Reference Orbit Event File."""

import copy
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
from .eo_oper_mpl_orbref_0203 import (  # noqa: F401
    EarthExplorerFile as MplOrbRefFileV0203,
)
from .eo_oper_mpl_orbref_0300 import (  # noqa: F401
    EarthObservationFile as MplOrbRefFileV0300,
)


_type_name = "MplOrbRefFile"
_type_description = __doc__.rstrip(".")
_type_classes = tuple(
    clazz for name, clazz in sorted(globals().items(), reverse=True)
    if name.startswith(_type_name)
)


def from_string(source: Union[str, bytes]):
    """Load a Reference Orbit Event from the source string or bytes string."""
    parser = XmlParser()

    if isinstance(source, str):
        parse = parser.from_string
    elif isinstance(source, bytes):
        parse = parser.from_bytes
    else:
        raise ValueError(
            f"invalid 'source' type ({type(source)!r}), str or bytes expected"
        )

    for clazz in _type_classes:
        try:
            return parse(source, clazz)
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to load {_type_description}")


def _from_xml(source):
    xmldoc = source
    source = copy.deepcopy(xmldoc)

    parser = XmlParser()
    for clazz in _type_classes:
        # see https://github.com/tefra/xsdata/issues/683
        source = copy.deepcopy(xmldoc)
        try:
            return parser.parse(source, clazz)
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to load {_type_description} form XML")


def load(source):
    """Load a Reference Orbit Event from the source stream.

    The input stream can be a filename, a file like object (open in
    binary mode) or an xml ElementTree (lxml is needed for the latter).
    """
    if hasattr(source, "read"):
        return from_string(source.read())
    elif hasattr(source, "getroot") or hasattr(source, "tag"):
        return _from_xml(source)

    parser = XmlParser()
    for clazz in _type_classes:
        try:
            return parser.parse(source, clazz)
        except ParserError:
            pass
    else:
        raise ParserError(f"Unable to load {_type_description} form {source}")
