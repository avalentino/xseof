from dataclasses import dataclass
from .attitude_header_type import AttitudeHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationHeader(AttitudeHeaderType):
    class Meta:
        name = "Earth_Observation_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
