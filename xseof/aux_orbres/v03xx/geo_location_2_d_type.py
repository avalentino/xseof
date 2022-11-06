from dataclasses import dataclass, field
from typing import Optional
from .latitude_type import LatitudeType
from .longitude_type import LongitudeType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


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
