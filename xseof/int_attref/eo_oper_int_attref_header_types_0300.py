from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .basic_types_0300 import AnyTypeType
from .header_types_0300 import FixedHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AttitudeHeaderType:
    class Meta:
        name = "Attitude_Header_Type"

    fixed_header: Optional[FixedHeaderType] = field(
        default=None,
        metadata={
            "name": "Fixed_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    variable_header: Optional[AnyTypeType] = field(
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
class EarthObservationHeader(AttitudeHeaderType):
    class Meta:
        name = "Earth_Observation_Header"
        namespace = "http://eop-cfi.esa.int/CFI"
