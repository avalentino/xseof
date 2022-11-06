from dataclasses import dataclass, field
from typing import Optional
from .row_type import RowType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class MatrixModelType:
    class Meta:
        name = "Matrix_Model_Type"

    row_1: Optional[RowType] = field(
        default=None,
        metadata={
            "name": "Row_1",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    row_2: Optional[RowType] = field(
        default=None,
        metadata={
            "name": "Row_2",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    row_3: Optional[RowType] = field(
        default=None,
        metadata={
            "name": "Row_3",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
