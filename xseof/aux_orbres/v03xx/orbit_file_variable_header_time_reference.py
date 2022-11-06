from enum import Enum

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


class OrbitFileVariableHeaderTimeReference(Enum):
    TAI = "TAI"
    UTC = "UTC"
    UT1 = "UT1"
