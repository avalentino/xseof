from dataclasses import dataclass
from .distance_type import DistanceType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class HeightType(DistanceType):
    class Meta:
        name = "Height_Type"
