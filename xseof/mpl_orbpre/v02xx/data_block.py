from dataclasses import dataclass
from .predicted_orbit_data_block_type import PredictedOrbitDataBlockType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DataBlock(PredictedOrbitDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
