from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from ..common.basic_types_0100 import AnyTypeType
from .eo_oper_mpl_orbpre_data_block_types_0100 import PredictedOrbitDataBlockType
from ..common.header_types_0100 import FixedHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DorisPreliminaryHeaderType:
    class Meta:
        name = "Doris_Preliminary_Header_Type"

    fixed_header: Optional[FixedHeaderType] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    variable_header: Optional[AnyTypeType] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


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
    data_block: Optional[PredictedOrbitDataBlockType] = field(
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
