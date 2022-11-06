from dataclasses import dataclass
from .doris_preliminary_file_type import DorisPreliminaryFileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthObservationFile(DorisPreliminaryFileType):
    class Meta:
        name = "Earth_Observation_File"
        namespace = "http://eop-cfi.esa.int/CFI"
