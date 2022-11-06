from dataclasses import dataclass, field
from typing import Optional
from .angle_type import AngleType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AngleModelType:
    class Meta:
        name = "Angle_Model_Type"

    angle_1: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Angle_1",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    angle_2: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Angle_2",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    angle_3: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Angle_3",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
