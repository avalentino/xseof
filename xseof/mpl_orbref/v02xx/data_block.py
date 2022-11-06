from dataclasses import dataclass
from .orbit_event_data_block_type import OrbitEventDataBlockType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DataBlock(OrbitEventDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
