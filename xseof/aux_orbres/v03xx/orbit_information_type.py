from dataclasses import dataclass, field
from typing import Optional
from .equator_cross_long_type import EquatorCrossLongType
from .rel_time_asc_node_type import RelTimeAscNodeType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitInformationType:
    class Meta:
        name = "Orbit_Information_Type"

    sensing_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sensing_Start",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"TAI=.*",
        }
    )
    abs_orbit_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "Abs_Orbit_Start",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    rel_time_asc_node_start: Optional[RelTimeAscNodeType] = field(
        default=None,
        metadata={
            "name": "Rel_Time_ASC_Node_Start",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    sensing_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sensing_Stop",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"TAI=.*",
        }
    )
    abs_orbit_stop: Optional[int] = field(
        default=None,
        metadata={
            "name": "Abs_Orbit_Stop",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    rel_time_asc_node_stop: Optional[RelTimeAscNodeType] = field(
        default=None,
        metadata={
            "name": "Rel_Time_ASC_Node_Stop",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    equator_cross_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Equator_Cross_Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    equator_cross_long: Optional[EquatorCrossLongType] = field(
        default=None,
        metadata={
            "name": "Equator_Cross_Long",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    ascending_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ascending_Flag",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "length": 1,
        }
    )
