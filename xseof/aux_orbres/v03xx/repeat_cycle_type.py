from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class RepeatCycleType:
    class Meta:
        name = "Repeat_Cycle_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="day",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
