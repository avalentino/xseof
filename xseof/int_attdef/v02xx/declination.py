from dataclasses import dataclass
from .angle_type import AngleType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class Declination(AngleType):
    pass
