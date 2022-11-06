from dataclasses import dataclass, field
from typing import List, Optional
from .angle_model_type import AngleModelType
from .file_model2_type import FileModel2Type
from .harmonic_model_type import HarmonicModelType
from .matrix_model_type import MatrixModelType
from .offsets_type import OffsetsType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class InstrAttType:
    class Meta:
        name = "Instr_Att_Type"

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
    offsets: List[OffsetsType] = field(
        default_factory=list,
        metadata={
            "name": "Offsets",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "max_occurs": 3,
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
