from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AnyTypeType:
    class Meta:
        name = "AnyType_Type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
