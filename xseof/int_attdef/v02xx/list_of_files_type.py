from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ListOfFilesType:
    class Meta:
        name = "List_of_Files_Type"

    file: List[str] = field(
        default_factory=list,
        metadata={
            "name": "File",
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
