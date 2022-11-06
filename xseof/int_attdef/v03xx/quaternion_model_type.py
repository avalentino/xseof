from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from .angle_time_type import AngleTimeType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class QuaternionModelType:
    class Meta:
        name = "Quaternion_Model_Type"

    reference_frame: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference_Frame",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_quaternions: Optional["QuaternionModelType.ListOfQuaternions"] = field(
        default=None,
        metadata={
            "name": "List_of_Quaternions",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )

    @dataclass
    class ListOfQuaternions:
        quaternion: List["QuaternionModelType.ListOfQuaternions.Quaternion"] = field(
            default_factory=list,
            metadata={
                "name": "Quaternion",
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

        @dataclass
        class Quaternion:
            time: Optional[AngleTimeType] = field(
                default=None,
                metadata={
                    "name": "Time",
                    "type": "Element",
                    "namespace": "http://eop-cfi.esa.int/CFI",
                    "required": True,
                }
            )
            q1: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Q1",
                    "type": "Element",
                    "namespace": "http://eop-cfi.esa.int/CFI",
                    "required": True,
                }
            )
            q2: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Q2",
                    "type": "Element",
                    "namespace": "http://eop-cfi.esa.int/CFI",
                    "required": True,
                }
            )
            q3: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Q3",
                    "type": "Element",
                    "namespace": "http://eop-cfi.esa.int/CFI",
                    "required": True,
                }
            )
            q4: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Q4",
                    "type": "Element",
                    "namespace": "http://eop-cfi.esa.int/CFI",
                    "required": True,
                }
            )
