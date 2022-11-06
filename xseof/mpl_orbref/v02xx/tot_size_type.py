from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class TotSizeType:
    class Meta:
        name = "Tot_Size_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="bytes",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
