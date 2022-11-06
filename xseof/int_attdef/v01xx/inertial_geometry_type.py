from dataclasses import dataclass, field
from typing import Optional
from .azimuth_type import AzimuthType
from .height_type import HeightType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class InertialGeometryType:
    class Meta:
        name = "Inertial_Geometry_Type"

    azimuth: Optional[AzimuthType] = field(
        default=None,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    altitude: Optional[HeightType] = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
