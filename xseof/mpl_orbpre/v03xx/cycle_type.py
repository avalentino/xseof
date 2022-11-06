from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from .cycle_length_type import CycleLengthType
from .longitude_type import LongitudeType
from .mlst_drift_type import MlstDriftType
from .mlst_nonlinear_drift_type import MlstNonlinearDriftType
from .repeat_cycle_type import RepeatCycleType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class CycleType:
    class Meta:
        name = "Cycle_Type"

    repeat_cycle: Optional[RepeatCycleType] = field(
        default=None,
        metadata={
            "name": "Repeat_Cycle",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    cycle_length: Optional[CycleLengthType] = field(
        default=None,
        metadata={
            "name": "Cycle_Length",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    anx_longitude: Optional[LongitudeType] = field(
        default=None,
        metadata={
            "name": "ANX_Longitude",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    mlst: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "MLST",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    mlst_drift: Optional[MlstDriftType] = field(
        default=None,
        metadata={
            "name": "MLST_Drift",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    mlst_nonlinear_drift: Optional[MlstNonlinearDriftType] = field(
        default=None,
        metadata={
            "name": "MLST_Nonlinear_Drift",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
