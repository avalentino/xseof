from dataclasses import dataclass
from .predicted_orbit_header_type import PredictedOrbitHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationHeader(PredictedOrbitHeaderType):
    class Meta:
        name = "Earth_Observation_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
