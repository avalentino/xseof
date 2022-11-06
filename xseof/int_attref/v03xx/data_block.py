from dataclasses import dataclass
from .attitude_data_block_type import AttitudeDataBlockType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DataBlock(AttitudeDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
