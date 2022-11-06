from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .att_type import AttType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class DataBlockType:
    class Meta:
        name = "Data_Block_Type"

    attitude_definition: Optional[AttType] = field(
        default=None,
        metadata={
            "name": "Attitude_Definition",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    type: str = field(
        init=False,
        default="xml",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        }
    )
