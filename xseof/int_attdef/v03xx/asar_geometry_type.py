from dataclasses import dataclass, field
from typing import Optional
from .asar_pulse_type import AsarPulseType
from .pointing_geometry_type import PointingGeometryType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AsarGeometryType:
    class Meta:
        name = "Asar_Geometry_Type"

    left_pt: Optional[PointingGeometryType] = field(
        default=None,
        metadata={
            "name": "Left_Pt",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    mid_pt: Optional[PointingGeometryType] = field(
        default=None,
        metadata={
            "name": "Mid_Pt",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    right_pt: Optional[PointingGeometryType] = field(
        default=None,
        metadata={
            "name": "Right_Pt",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    narrow_asar: Optional["AsarGeometryType.NarrowAsar"] = field(
        default=None,
        metadata={
            "name": "Narrow_Asar",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    wide_asar: Optional["AsarGeometryType.WideAsar"] = field(
        default=None,
        metadata={
            "name": "Wide_Asar",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )

    @dataclass
    class NarrowAsar:
        slant_range_left: Optional[AsarPulseType] = field(
            default=None,
            metadata={
                "name": "Slant_Range_Left",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
                "required": True,
            }
        )

    @dataclass
    class WideAsar:
        slant_range_left: Optional[AsarPulseType] = field(
            default=None,
            metadata={
                "name": "Slant_Range_Left",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
                "required": True,
            }
        )
        slant_range_right: Optional[AsarPulseType] = field(
            default=None,
            metadata={
                "name": "Slant_Range_Right",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
                "required": True,
            }
        )
