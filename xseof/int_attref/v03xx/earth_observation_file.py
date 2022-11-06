from dataclasses import dataclass
from .attitude_file_type import AttitudeFileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationFile(AttitudeFileType):
    class Meta:
        name = "Earth_Observation_File"
        namespace = "http://eop-cfi.esa.int/CFI"
