from dataclasses import dataclass, field
from typing import Optional
from .time_reference_type import TimeReferenceType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AngleTimeType:
    class Meta:
        name = "Angle_Time_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[A-Z0-9]{3}=(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}|0000-00-00T00:00:00|9999-99-99T99:99:99)(.\d*)?",
        }
    )
    ref: Optional[TimeReferenceType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
