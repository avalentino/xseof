from dataclasses import dataclass, field
from typing import List, Optional
from .basic_types_0201 import (
    AngleType,
    HeightType,
)

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AzimuthType(AngleType):
    class Meta:
        name = "Azimuth_Type"


@dataclass
class ElevationType(AngleType):
    class Meta:
        name = "Elevation_Type"


@dataclass
class LatitudeType(AngleType):
    class Meta:
        name = "Latitude_Type"


@dataclass
class LongitudeType(AngleType):
    class Meta:
        name = "Longitude_Type"


@dataclass
class MispointingAnglesType:
    class Meta:
        name = "Mispointing_Angles_Type"

    pitch: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Pitch",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    roll: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Roll",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    yaw: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Yaw",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class GeoLocation2DType:
    class Meta:
        name = "Geo_Location_2D_Type"

    long: Optional[LongitudeType] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    lat: Optional[LatitudeType] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class PointingDirectionType:
    class Meta:
        name = "Pointing_Direction_Type"

    az: Optional[AzimuthType] = field(
        default=None,
        metadata={
            "name": "Az",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    el: Optional[ElevationType] = field(
        default=None,
        metadata={
            "name": "El",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class GeoLocationType(GeoLocation2DType):
    class Meta:
        name = "Geo_Location_Type"

    alt: Optional[HeightType] = field(
        default=None,
        metadata={
            "name": "Alt",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class PolygonTypeType:
    class Meta:
        name = "Polygon_Type_Type"

    polygon_pt: List[GeoLocation2DType] = field(
        default_factory=list,
        metadata={
            "name": "Polygon_Pt",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
