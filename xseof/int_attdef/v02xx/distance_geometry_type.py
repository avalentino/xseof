from dataclasses import dataclass, field
from typing import Optional
from .azimuth_type import AzimuthType
from .distance_type import DistanceType
from .elevation_type import ElevationType
from .height_type import HeightType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DistanceGeometryType:
    class Meta:
        name = "Distance_Geometry_Type"

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
    distance: Optional[DistanceType] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
