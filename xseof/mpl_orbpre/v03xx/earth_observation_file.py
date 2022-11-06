from dataclasses import dataclass
from .predicted_orbit_file_type import PredictedOrbitFileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationFile(PredictedOrbitFileType):
    class Meta:
        name = "Earth_Observation_File"
        namespace = "http://eop-cfi.esa.int/CFI"
