from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AsarPulseType:
    class Meta:
        name = "Asar_Pulse_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="10e-6s",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
