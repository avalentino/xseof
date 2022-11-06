from dataclasses import dataclass, field
from typing import Optional
from .cycle_type import CycleType
from .orbit_type import OrbitType
from .time_of_anx_type import TimeOfAnxType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitChangeType:
    class Meta:
        name = "Orbit_Change_Type"

    orbit: Optional[OrbitType] = field(
        default=None,
        metadata={
            "name": "Orbit",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    cycle: Optional[CycleType] = field(
        default=None,
        metadata={
            "name": "Cycle",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    time_of_anx: Optional[TimeOfAnxType] = field(
        default=None,
        metadata={
            "name": "Time_of_ANX",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
