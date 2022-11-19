from dataclasses import dataclass, field
from typing import Optional
from ..common.orbit_types_0100 import (
    ListOfOsvsType,
    ListOfOrbitChangesType,
)

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitReferenceDataBlockType:
    class Meta:
        name = "Orbit_Reference_Data_Block_Type"

    list_of_orbit_changes: Optional[ListOfOrbitChangesType] = field(
        default=None,
        metadata={
            "name": "List_of_Orbit_Changes",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_osvs: Optional[ListOfOsvsType] = field(
        default=None,
        metadata={
            "name": "List_of_OSVs",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
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
