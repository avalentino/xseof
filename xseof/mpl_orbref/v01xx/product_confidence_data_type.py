from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ProductConfidenceDataType:
    class Meta:
        name = "Product_Confidence_Data_Type"

    num_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_ISPs",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    num_missing_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_Missing_ISPs",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    num_error_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_Error_ISPs",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    num_discarded_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_Discarded_ISPs",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    num_rs_isps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_RS_ISPs",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    num_rs_corrections: Optional[int] = field(
        default=None,
        metadata={
            "name": "Num_RS_Corrections",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
