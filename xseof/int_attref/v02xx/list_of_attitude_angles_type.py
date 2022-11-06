from dataclasses import dataclass, field
from typing import List, Optional
from .angles_data_type import AnglesDataType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ListOfAttitudeAnglesType:
    class Meta:
        name = "List_of_Attitude_Angles_Type"

    attitude_angles: List[AnglesDataType] = field(
        default_factory=list,
        metadata={
            "name": "Attitude_Angles",
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
