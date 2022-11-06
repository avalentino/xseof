from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class MlstDriftType:
    class Meta:
        name = "MLST_Drift_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="s/day",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
