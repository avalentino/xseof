from dataclasses import dataclass
from .orbit_event_file_type import OrbitEventFileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationFile(OrbitEventFileType):
    class Meta:
        name = "Earth_Observation_File"
        namespace = "http://eop-cfi.esa.int/CFI"
