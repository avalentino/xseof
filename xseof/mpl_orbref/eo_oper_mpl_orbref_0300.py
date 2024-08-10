from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .eo_oper_mpl_orbref_data_block_types_0300 import (
    OrbitEventDataBlockType,
)
from .eo_oper_mpl_orbref_header_types_0300 import OrbitEventHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitEventFileType:
    class Meta:
        name = "Orbit_Event_File_Type"

    earth_observation_header: Optional[OrbitEventHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        },
    )
    data_block: Optional[OrbitEventDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        },
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EarthObservationFile(OrbitEventFileType):
    class Meta:
        name = "Earth_Observation_File"
        namespace = "http://eop-cfi.esa.int/CFI"
