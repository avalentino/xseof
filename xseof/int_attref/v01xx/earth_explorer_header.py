from dataclasses import dataclass
from .attitude_header_type import AttitudeHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthExplorerHeader(AttitudeHeaderType):
    class Meta:
        name = "Earth_Explorer_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
