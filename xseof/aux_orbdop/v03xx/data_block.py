from dataclasses import dataclass
from .doris_preliminary_data_block_type import DorisPreliminaryDataBlockType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DataBlock(DorisPreliminaryDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
