from dataclasses import dataclass, field
from typing import Optional
from .list_of_attitude_angles_type import ListOfAttitudeAnglesType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AttitudeAnglesDataType:
    class Meta:
        name = "Attitude_Angles_Data_Type"

    reference_frame: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference_Frame",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_attitude_angles: Optional[ListOfAttitudeAnglesType] = field(
        default=None,
        metadata={
            "name": "List_of_Attitude_Angles",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
