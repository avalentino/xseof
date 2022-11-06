from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .data_block_type import DataBlockType
from .header_type import HeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class FileType:
    class Meta:
        name = "File_Type"

    earth_observation_header: Optional[HeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[DataBlockType] = field(
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
