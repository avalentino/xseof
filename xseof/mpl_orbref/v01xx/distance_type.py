from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DistanceType:
    class Meta:
        name = "Distance_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="m",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
