from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .time_reference_type import TimeReferenceType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class TimeWindowType:
    class Meta:
        name = "Time_Window_Type"

    time_0: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Time_0",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    time_1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Time_1",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    time_ref: Optional[TimeReferenceType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
