from dataclasses import dataclass, field
from typing import Optional
from .geo_location_2_d_type import GeoLocation2DType
from .height_type import HeightType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


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
