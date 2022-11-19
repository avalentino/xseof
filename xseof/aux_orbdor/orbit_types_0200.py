from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from .geo_location_types_0200 import LongitudeType

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
class HarmonicTermType:
    class Meta:
        name = "Harmonic_Term_Type"

    reference_time: Optional["HarmonicTermType.ReferenceTime"] = field(
        default=None,
        metadata={
            "name": "Reference_Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    period: Optional["HarmonicTermType.Period"] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    amplitude_sin: Optional["HarmonicTermType.AmplitudeSin"] = field(
        default=None,
        metadata={
            "name": "Amplitude_Sin",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    amplitude_cos: Optional["HarmonicTermType.AmplitudeCos"] = field(
        default=None,
        metadata={
            "name": "Amplitude_Cos",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    seq: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class ReferenceTime:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r"(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}|0000-00-00T00:00:00|9999-99-99T99:99:99)(.\d*)?",
            }
        )
        time_ref: str = field(
            init=False,
            default="UT1",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Period:
        value: Optional[Decimal] = field(
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
    class AmplitudeSin:
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
    class AmplitudeCos:
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
class MlstNonlinearDriftType:
    class Meta:
        name = "MLST_Nonlinear_Drift_Type"

    linear_approx_validity: Optional["MlstNonlinearDriftType.LinearApproxValidity"] = field(
        default=None,
        metadata={
            "name": "Linear_Approx_Validity",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    quadratic_term: Optional["MlstNonlinearDriftType.QuadraticTerm"] = field(
        default=None,
        metadata={
            "name": "Quadratic_Term",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    harmonics_terms: Optional["MlstNonlinearDriftType.HarmonicsTerms"] = field(
        default=None,
        metadata={
            "name": "Harmonics_Terms",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )

    @dataclass
    class LinearApproxValidity:
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
    class QuadraticTerm:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s/day^2",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HarmonicsTerms:
        harmonic_term: List[HarmonicTermType] = field(
            default_factory=list,
            metadata={
                "name": "Harmonic_Term",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
                "max_occurs": 2,
            }
        )
        num: int = field(
            init=False,
            default=2,
            metadata={
                "type": "Attribute",
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
    mlst_nonlinear_drift: Optional[MlstNonlinearDriftType] = field(
        default=None,
        metadata={
            "name": "MLST_Nonlinear_Drift",
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
