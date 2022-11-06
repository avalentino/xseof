from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class TimeOfAnxType:
    class Meta:
        name = "Time_of_ANX_Type"

    tai: Optional[str] = field(
        default=None,
        metadata={
            "name": "TAI",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"TAI=.*",
        }
    )
    utc: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTC",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"UTC=.*",
        }
    )
    ut1: Optional[str] = field(
        default=None,
        metadata={
            "name": "UT1",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"UT1=.*",
        }
    )
