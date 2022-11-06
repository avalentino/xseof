from dataclasses import dataclass
from .seconds_time_type import SecondsTimeType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class SecondsDurationType(SecondsTimeType):
    class Meta:
        name = "Seconds_Duration_Type"
