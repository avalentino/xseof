from dataclasses import dataclass, field
from typing import List, Optional
from .geo_location_2_d_type import GeoLocation2DType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


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
