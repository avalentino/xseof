from dataclasses import dataclass
from .doris_preliminary_file_type import DorisPreliminaryFileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthExplorerFile(DorisPreliminaryFileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = "http://eop-cfi.esa.int/CFI"
