from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .angle_time_type import AngleTimeType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class QuaternionType:
    class Meta:
        name = "Quaternion_Type"

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
