from dataclasses import dataclass, field
from typing import Optional
from .lat_type import LatType
from .long_type import LongType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ProductLocationType:
    class Meta:
        name = "Product_Location_Type"

    start_lat: Optional[LatType] = field(
        default=None,
        metadata={
            "name": "Start_Lat",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    start_long: Optional[LongType] = field(
        default=None,
        metadata={
            "name": "Start_Long",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    stop_lat: Optional[LatType] = field(
        default=None,
        metadata={
            "name": "Stop_Lat",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    stop_long: Optional[LongType] = field(
        default=None,
        metadata={
            "name": "Stop_Long",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
