from dataclasses import dataclass
from .restituted_orbit_file_type import RestitutedOrbitFileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthExplorerFile(RestitutedOrbitFileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = "http://eop-cfi.esa.int/CFI"
