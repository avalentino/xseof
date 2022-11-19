from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class SecondsTimeType:
    class Meta:
        name = "Seconds_Time_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="s",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SecondsDurationType(SecondsTimeType):
    class Meta:
        name = "Seconds_Duration_Type"
