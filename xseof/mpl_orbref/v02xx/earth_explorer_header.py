from dataclasses import dataclass
from .orbit_event_header_type import OrbitEventHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthExplorerHeader(OrbitEventHeaderType):
    class Meta:
        name = "Earth_Explorer_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
