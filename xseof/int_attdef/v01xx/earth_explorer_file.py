from dataclasses import dataclass
from .file_type import FileType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class EarthExplorerFile(FileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = "http://eop-cfi.esa.int/CFI"
