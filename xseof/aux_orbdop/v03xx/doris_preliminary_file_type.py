from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .doris_preliminary_data_block_type import DorisPreliminaryDataBlockType
from .doris_preliminary_header_type import DorisPreliminaryHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DorisPreliminaryFileType:
    class Meta:
        name = "Doris_Preliminary_File_Type"

    earth_observation_header: Optional[DorisPreliminaryHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[DorisPreliminaryDataBlockType] = field(
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
