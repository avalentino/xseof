from dataclasses import dataclass
from .angle_type import AngleType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class LatitudeType(AngleType):
    class Meta:
        name = "Latitude_Type"
