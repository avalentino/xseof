from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from .harmonic_term_type import HarmonicTermType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class MlstNonlinearDriftType:
    class Meta:
        name = "MLST_Nonlinear_Drift_Type"

    linear_approx_validity: Optional["MlstNonlinearDriftType.LinearApproxValidity"] = field(
        default=None,
        metadata={
            "name": "Linear_Approx_Validity",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    quadratic_term: Optional["MlstNonlinearDriftType.QuadraticTerm"] = field(
        default=None,
        metadata={
            "name": "Quadratic_Term",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    harmonics_terms: Optional["MlstNonlinearDriftType.HarmonicsTerms"] = field(
        default=None,
        metadata={
            "name": "Harmonics_Terms",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )

    @dataclass
    class LinearApproxValidity:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="orbit",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class QuadraticTerm:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s/day^2",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HarmonicsTerms:
        harmonic_term: List[HarmonicTermType] = field(
            default_factory=list,
            metadata={
                "name": "Harmonic_Term",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
                "max_occurs": 2,
            }
        )
        num: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
