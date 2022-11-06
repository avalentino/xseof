from dataclasses import dataclass
from .doris_precise_data_block_type import DorisPreciseDataBlockType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DataBlock(DorisPreciseDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
