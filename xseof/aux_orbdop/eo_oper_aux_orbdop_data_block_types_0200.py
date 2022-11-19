from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from ..common.orbit_types_0200 import ListOfOsvsType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DorisPreliminaryDataBlockType:
    class Meta:
        name = "Doris_Preliminary_Data_Block_Type"

    list_of_osvs: Optional[ListOfOsvsType] = field(
        default=None,
        metadata={
            "name": "List_of_OSVs",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    type: str = field(
        init=False,
        default="xml",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        }
    )


@dataclass
class DataBlock(DorisPreliminaryDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
