from dataclasses import dataclass, field
from typing import List, Optional
from .harmonic_type import HarmonicType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ListOfHarmonicsType:
    class Meta:
        name = "List_of_Harmonics_Type"

    harmonic: List[HarmonicType] = field(
        default_factory=list,
        metadata={
            "name": "Harmonic",
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
