from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .eo_oper_aux_orbres_data_block_types_0300 import RestitutedOrbitDataBlockType
from .eo_oper_aux_orbres_header_types_0300 import RestitutedOrbitHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class RestitutedOrbitFileType:
    class Meta:
        name = "Restituted_Orbit_File_Type"

    earth_observation_header: Optional[RestitutedOrbitHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[RestitutedOrbitDataBlockType] = field(
        default=None,
        metadata={
            "name": "Data_Block",
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
            "required": True,
        }
    )


@dataclass
class EarthObservationFile(RestitutedOrbitFileType):
    class Meta:
        name = "Earth_Observation_File"
        namespace = "http://eop-cfi.esa.int/CFI"
