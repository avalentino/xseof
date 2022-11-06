from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class VelocityComponentType:
    class Meta:
        name = "Velocity_Component_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="m/s",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
