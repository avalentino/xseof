from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .eo_oper_aux_orbdor_data_block_types_0200 import DorisPreciseDataBlockType
from .eo_oper_aux_orbdor_header_types_0200 import DorisPreciseHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DorisPreciseFileType:
    class Meta:
        name = "Doris_Precise_File_Type"

    earth_explorer_header: Optional[DorisPreciseHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
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


@dataclass
class EarthExplorerFile(DorisPreciseFileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = "http://eop-cfi.esa.int/CFI"
