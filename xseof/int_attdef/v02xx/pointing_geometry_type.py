from dataclasses import dataclass, field
from typing import Optional
from .azimuth_type import AzimuthType
from .elevation_type import ElevationType
from .height_type import HeightType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class PointingGeometryType:
    class Meta:
        name = "Pointing_Geometry_Type"

    azimuth: Optional[AzimuthType] = field(
        default=None,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    elevation: Optional[ElevationType] = field(
        default=None,
        metadata={
            "name": "Elevation",
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
