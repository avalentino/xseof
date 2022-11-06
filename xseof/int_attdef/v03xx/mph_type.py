from dataclasses import dataclass, field
from typing import Optional
from .delta_ut1_type import DeltaUt1Type
from .position_type import PositionType
from .tot_size_type import TotSizeType
from .velocity_type import VelocityType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class MphType:
    class Meta:
        name = "MPH_Type"

    product: Optional[str] = field(
        default=None,
        metadata={
            "name": "Product",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    proc_stage_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Proc_Stage_Code",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    ref_doc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref_Doc",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    proc_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Proc_Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    software_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Software_Version",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    cycle: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cycle",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    rel_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Rel_Orbit",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    abs_orbit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Abs_Orbit",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    state_vector_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "State_Vector_Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"UTC=.*",
        }
    )
    delta_ut1: Optional[DeltaUt1Type] = field(
        default=None,
        metadata={
            "name": "Delta_UT1",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    x_position: Optional[PositionType] = field(
        default=None,
        metadata={
            "name": "X_Position",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    y_position: Optional[PositionType] = field(
        default=None,
        metadata={
            "name": "Y_Position",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    z_position: Optional[PositionType] = field(
        default=None,
        metadata={
            "name": "Z_Position",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    x_velocity: Optional[VelocityType] = field(
        default=None,
        metadata={
            "name": "X_Velocity",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    y_velocity: Optional[VelocityType] = field(
        default=None,
        metadata={
            "name": "Y_Velocity",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    z_velocity: Optional[VelocityType] = field(
        default=None,
        metadata={
            "name": "Z_Velocity",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    state_vector_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "State_Vector_Source",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"..",
        }
    )
    product_err: Optional[int] = field(
        default=None,
        metadata={
            "name": "Product_Err",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    tot_size: Optional[TotSizeType] = field(
        default=None,
        metadata={
            "name": "Tot_Size",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
