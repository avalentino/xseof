from dataclasses import dataclass, field
from typing import Optional
from .list_of_quaternions_type import ListOfQuaternionsType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class QuaternionDataType:
    class Meta:
        name = "Quaternion_Data_Type"

    reference_frame: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference_Frame",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_quaternions: Optional[ListOfQuaternionsType] = field(
        default=None,
        metadata={
            "name": "List_of_Quaternions",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
