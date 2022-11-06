from dataclasses import dataclass, field
from typing import Optional
from .azimuth_type import AzimuthType
from .elevation_type import ElevationType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


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
