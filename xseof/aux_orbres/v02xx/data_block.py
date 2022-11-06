from dataclasses import dataclass
from .restituted_orbit_data_block_type import RestitutedOrbitDataBlockType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DataBlock(RestitutedOrbitDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
