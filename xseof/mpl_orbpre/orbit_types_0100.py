from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from .geo_location_types_0100 import LongitudeType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class CycleLengthType:
    class Meta:
        name = "Cycle_Length_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="orbit",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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


@dataclass
class PositionComponentType:
    class Meta:
        name = "Position_Component_Type"

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


@dataclass
class RepeatCycleType:
    class Meta:
        name = "Repeat_Cycle_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="day",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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


@dataclass
class CycleType:
    class Meta:
        name = "Cycle_Type"

    repeat_cycle: Optional[RepeatCycleType] = field(
        default=None,
        metadata={
            "name": "Repeat_Cycle",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    cycle_length: Optional[CycleLengthType] = field(
        default=None,
        metadata={
            "name": "Cycle_Length",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    anx_longitude: Optional[LongitudeType] = field(
        default=None,
        metadata={
            "name": "ANX_Longitude",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    mlst: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "MLST",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    mlst_drift: Optional[MlstDriftType] = field(
        default=None,
        metadata={
            "name": "MLST_Drift",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


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


@dataclass
class ListOfOsvsType:
    class Meta:
        name = "List_of_OSVs_Type"

    osv: List[OsvType] = field(
        default_factory=list,
        metadata={
            "name": "OSV",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "min_occurs": 1,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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


@dataclass
class ListOfOrbitChangesType:
    class Meta:
        name = "List_of_Orbit_Changes_Type"

    orbit_change: List[OrbitChangeType] = field(
        default_factory=list,
        metadata={
            "name": "Orbit_Change",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "min_occurs": 1,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
