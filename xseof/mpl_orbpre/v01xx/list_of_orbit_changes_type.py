from dataclasses import dataclass, field
from typing import List, Optional
from .orbit_change_type import OrbitChangeType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ListOfOrbitChangesType:
    class Meta:
        name = "List_of_Orbit_Changes_Type"

    orbit_change: List[OrbitChangeType] = field(
        default_factory=list,
        metadata={
            "name": "Orbit_Change",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "min_occurs": 1,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
