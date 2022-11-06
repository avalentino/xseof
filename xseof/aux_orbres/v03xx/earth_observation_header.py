from dataclasses import dataclass
from .restituted_orbit_header_type import RestitutedOrbitHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationHeader(RestitutedOrbitHeaderType):
    class Meta:
        name = "Earth_Observation_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
