from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .restituted_orbit_data_block_type import RestitutedOrbitDataBlockType
from .restituted_orbit_header_type import RestitutedOrbitHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class RestitutedOrbitFileType:
    class Meta:
        name = "Restituted_Orbit_File_Type"

    earth_explorer_header: Optional[RestitutedOrbitHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Explorer_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[RestitutedOrbitDataBlockType] = field(
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
