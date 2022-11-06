from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .doris_precise_data_block_type import DorisPreciseDataBlockType
from .doris_precise_header_type import DorisPreciseHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DorisPreciseFileType:
    class Meta:
        name = "Doris_Precise_File_Type"

    earth_observation_header: Optional[DorisPreciseHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[DorisPreciseDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )
