from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AnyTypeType:
    class Meta:
        name = "AnyType_Type"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
