from dataclasses import dataclass, field
from typing import List, Optional
from .quaternion_type import QuaternionType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ListOfQuaternionsType:
    class Meta:
        name = "List_of_Quaternions_Type"

    quaternions: List[QuaternionType] = field(
        default_factory=list,
        metadata={
            "name": "Quaternions",
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
