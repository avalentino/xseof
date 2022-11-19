from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from ..common.header_types_0200 import (
    FixedHeaderType,
    OrbitFileVariableHeader,
)

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitEventHeaderType:
    class Meta:
        name = "Orbit_Event_Header_Type"

    fixed_header: Optional[FixedHeaderType] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    variable_header: Optional[OrbitFileVariableHeader] = field(
        default=None,
        metadata={
            "name": "Variable_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
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


@dataclass
class EarthExplorerHeader(OrbitEventHeaderType):
    class Meta:
        name = "Earth_Explorer_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
