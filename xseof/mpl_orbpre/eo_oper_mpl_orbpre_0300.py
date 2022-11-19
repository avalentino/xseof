from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .eo_oper_mpl_orbpre_data_block_types_0300 import PredictedOrbitDataBlockType
from .eo_oper_mpl_orbpre_header_types_0300 import PredictedOrbitHeaderType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class PredictedOrbitFileType:
    class Meta:
        name = "Predicted_Orbit_File_Type"

    earth_observation_header: Optional[PredictedOrbitHeaderType] = field(
        default=None,
        metadata={
            "name": "Earth_Observation_Header",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    data_block: Optional[PredictedOrbitDataBlockType] = field(
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
class EarthObservationFile(PredictedOrbitFileType):
    class Meta:
        name = "Earth_Observation_File"
        namespace = "http://eop-cfi.esa.int/CFI"
