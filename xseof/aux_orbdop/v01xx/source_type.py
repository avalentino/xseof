from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class SourceType:
    class Meta:
        name = "Source_Type"

    system: Optional[str] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    creator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creator",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    creator_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creator_Version",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creation_Date",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "length": 23,
            "pattern": r"UTC=.*",
        }
    )
