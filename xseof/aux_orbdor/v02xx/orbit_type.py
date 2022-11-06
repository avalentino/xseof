from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitType:
    class Meta:
        name = "Orbit_Type"

    absolute_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Absolute_Orbit",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    relative_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Relative_Orbit",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    cycle_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cycle_Number",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    phase_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Phase_Number",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
