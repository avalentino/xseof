from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class RowType:
    class Meta:
        name = "Row_Type"

    column_1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Column_1",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    column_2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Column_2",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    column_3: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Column_3",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
