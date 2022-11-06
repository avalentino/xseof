from dataclasses import dataclass, field
from typing import Optional
from .freq_type import FreqType
from .refraction_model_type import RefractionModelType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class RefractionType:
    class Meta:
        name = "Refraction_Type"

    model: Optional[RefractionModelType] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    freq: Optional[FreqType] = field(
        default=None,
        metadata={
            "name": "Freq",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
