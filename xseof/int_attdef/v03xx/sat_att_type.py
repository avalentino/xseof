from dataclasses import dataclass, field
from typing import Optional
from .angle_model_type import AngleModelType
from .file_model_type import FileModelType
from .harmonic_model_type import HarmonicModelType
from .matrix_model_type import MatrixModelType
from .quaternion_model_type import QuaternionModelType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class SatAttType:
    class Meta:
        name = "Sat_Att_Type"

    none: Optional[str] = field(
        default=None,
        metadata={
            "name": "None",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "length": 0,
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
    quaternion_plus_angle: Optional["SatAttType.QuaternionPlusAngle"] = field(
        default=None,
        metadata={
            "name": "Quaternion_Plus_Angle",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    quaternion_plus_matrix: Optional["SatAttType.QuaternionPlusMatrix"] = field(
        default=None,
        metadata={
            "name": "Quaternion_Plus_Matrix",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )

    @dataclass
    class QuaternionPlusAngle:
        angle_model: Optional[AngleModelType] = field(
            default=None,
            metadata={
                "name": "Angle_Model",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
                "required": True,
            }
        )
        quaternion_data: Optional[QuaternionModelType] = field(
            default=None,
            metadata={
                "name": "Quaternion_Data",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
            }
        )
        quaternion_file: Optional[str] = field(
            default=None,
            metadata={
                "name": "Quaternion_File",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
            }
        )

    @dataclass
    class QuaternionPlusMatrix:
        matrix_model: Optional[MatrixModelType] = field(
            default=None,
            metadata={
                "name": "Matrix_Model",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
                "required": True,
            }
        )
        quaternion_data: Optional[QuaternionModelType] = field(
            default=None,
            metadata={
                "name": "Quaternion_Data",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
            }
        )
        quaternion_file: Optional[str] = field(
            default=None,
            metadata={
                "name": "Quaternion_File",
                "type": "Element",
                "namespace": "http://eop-cfi.esa.int/CFI",
            }
        )
