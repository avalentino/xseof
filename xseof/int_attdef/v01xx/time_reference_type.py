from enum import Enum

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


class TimeReferenceType(Enum):
    UTC = "UTC"
    UT1 = "UT1"
    TAI = "TAI"
    GPS = "GPS"
