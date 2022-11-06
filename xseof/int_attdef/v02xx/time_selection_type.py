from dataclasses import dataclass, field
from typing import Optional
from .time_window_type import TimeWindowType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class TimeSelectionType:
    class Meta:
        name = "Time_Selection_Type"

    select_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "Select_File",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "length": 0,
        }
    )
    time_window: Optional[TimeWindowType] = field(
        default=None,
        metadata={
            "name": "Time_Window",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
