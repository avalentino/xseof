from dataclasses import dataclass, field
from typing import List, Optional
from .osv_type import OsvType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ListOfOsvsType:
    class Meta:
        name = "List_of_OSVs_Type"

    osv: List[OsvType] = field(
        default_factory=list,
        metadata={
            "name": "OSV",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "min_occurs": 1,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
