from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .attitude_data_block_type import AttitudeDataBlockType
from .attitude_header_type import AttitudeHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AttitudeFileType:
    class Meta:
        name = "Attitude_File_Type"

    earth_observation_header: Optional[AttitudeHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[AttitudeDataBlockType] = field(
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
