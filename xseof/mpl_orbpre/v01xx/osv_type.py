from dataclasses import dataclass, field
from typing import Optional
from .position_component_type import PositionComponentType
from .velocity_component_type import VelocityComponentType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OsvType:
    class Meta:
        name = "OSV_Type"

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
    absolute_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Absolute_Orbit",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    x: Optional[PositionComponentType] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    y: Optional[PositionComponentType] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    z: Optional[PositionComponentType] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    vx: Optional[VelocityComponentType] = field(
        default=None,
        metadata={
            "name": "VX",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    vy: Optional[VelocityComponentType] = field(
        default=None,
        metadata={
            "name": "VY",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    vz: Optional[VelocityComponentType] = field(
        default=None,
        metadata={
            "name": "VZ",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "Quality",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
