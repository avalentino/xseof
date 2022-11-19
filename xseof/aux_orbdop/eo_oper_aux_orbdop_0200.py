from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .eo_oper_aux_orbdop_data_block_types_0200 import DorisPreliminaryDataBlockType
from .eo_oper_aux_orbdop_header_types_0200 import DorisPreliminaryHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DorisPreliminaryFileType:
    class Meta:
        name = "Doris_Preliminary_File_Type"

    earth_explorer_header: Optional[DorisPreliminaryHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
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


@dataclass
class EarthExplorerFile(DorisPreliminaryFileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = "http://eop-cfi.esa.int/CFI"
