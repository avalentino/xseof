from dataclasses import dataclass, field
from typing import Optional
from .angle_time_type import AngleTimeType
from .angle_type import AngleType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AnglesDataType:
    class Meta:
        name = "Angles_Data_Type"

    time: Optional[AngleTimeType] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    pitch: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Pitch",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    roll: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Roll",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    yaw: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Yaw",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
