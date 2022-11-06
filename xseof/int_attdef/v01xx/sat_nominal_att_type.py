from dataclasses import dataclass, field
from typing import Optional
from .aocs_type import AocsType
from .file_model2_type import FileModel2Type
from .harmonic_model_type import HarmonicModelType
from .param_model_type import ParamModelType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class SatNominalAttType:
    class Meta:
        name = "Sat_Nominal_Att_Type"

    none: Optional[str] = field(
        default=None,
        metadata={
            "name": "None",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "length": 0,
        }
    )
    aocs_model: Optional[AocsType] = field(
        default=None,
        metadata={
            "name": "AOCS_Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    parameter_model: Optional[ParamModelType] = field(
        default=None,
        metadata={
            "name": "Parameter_Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    harmonic_model: Optional[HarmonicModelType] = field(
        default=None,
        metadata={
            "name": "Harmonic_Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    file_model: Optional[FileModel2Type] = field(
        default=None,
        metadata={
            "name": "File_Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
