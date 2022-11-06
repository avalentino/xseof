from dataclasses import dataclass
from .doris_precise_header_type import DorisPreciseHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationHeader(DorisPreciseHeaderType):
    class Meta:
        name = "Earth_Observation_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
