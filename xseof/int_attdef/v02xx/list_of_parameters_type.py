from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ListOfParametersType:
    class Meta:
        name = "List_of_Parameters_Type"

    parameter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
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
