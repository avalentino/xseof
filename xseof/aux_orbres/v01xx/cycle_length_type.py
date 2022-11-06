from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class CycleLengthType:
    class Meta:
        name = "Cycle_Length_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="orbit",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
