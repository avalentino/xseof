from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .basic_types_0100 import AnyTypeType
from .eo_oper_mpl_orbref_data_block_types_0100 import OrbitReferenceDataBlockType
from .header_types_0100 import FixedHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitReferenceHeaderType:
    class Meta:
        name = "Orbit_Reference_Header_Type"

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
class OrbitReferenceFileType:
    class Meta:
        name = "Orbit_Reference_File_Type"

    earth_explorer_header: Optional[OrbitReferenceHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[OrbitReferenceDataBlockType] = field(
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
class EarthExplorerFile(OrbitReferenceFileType):
    class Meta:
        name = "Earth_Explorer_File"
        namespace = "http://eop-cfi.esa.int/CFI"
