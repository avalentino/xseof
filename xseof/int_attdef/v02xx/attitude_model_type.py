from dataclasses import dataclass, field
from typing import Optional
from .angle_model_type import AngleModelType
from .aocs_type import AocsType
from .file_model_type import FileModelType
from .harmonic_model_type import HarmonicModelType
from .matrix_model_type import MatrixModelType
from .param_model_type import ParamModelType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AttitudeModelType:
    class Meta:
        name = "Attitude_Model_Type"

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
    file_model: Optional[FileModelType] = field(
        default=None,
        metadata={
            "name": "File_Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    angle_model: Optional[AngleModelType] = field(
        default=None,
        metadata={
            "name": "Angle_Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    matrix_model: Optional[MatrixModelType] = field(
        default=None,
        metadata={
            "name": "Matrix_Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
