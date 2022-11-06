from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class HarmonicType:
    class Meta:
        name = "Harmonic_Type"

    harmonic_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "Harmonic_Type",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    harmonic_coef: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Harmonic_Coef",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
