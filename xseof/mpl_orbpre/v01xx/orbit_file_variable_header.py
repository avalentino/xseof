from dataclasses import dataclass, field
from typing import Optional
from .orbit_file_variable_header_ref_frame import OrbitFileVariableHeaderRefFrame
from .orbit_file_variable_header_time_reference import OrbitFileVariableHeaderTimeReference

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitFileVariableHeader:
    class Meta:
        name = "Orbit_File_Variable_Header"

    ref_frame: Optional[OrbitFileVariableHeaderRefFrame] = field(
        default=None,
        metadata={
            "name": "Ref_Frame",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    time_reference: Optional[OrbitFileVariableHeaderTimeReference] = field(
        default=None,
        metadata={
            "name": "Time_Reference",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
