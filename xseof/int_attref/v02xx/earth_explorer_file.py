from dataclasses import dataclass
from .attitude_file_type import AttitudeFileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthExplorerFile(AttitudeFileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = "http://eop-cfi.esa.int/CFI"
