from dataclasses import dataclass, field
from typing import Optional
from .harmonic_model_type_angle_type import HarmonicModelTypeAngleType
from .list_of_harmonics_type import ListOfHarmonicsType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class HarmonicModelType:
    class Meta:
        name = "Harmonic_Model_Type"

    angle_type: Optional[HarmonicModelTypeAngleType] = field(
        default=None,
        metadata={
            "name": "Angle_Type",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_harmonics_pitch: Optional[ListOfHarmonicsType] = field(
        default=None,
        metadata={
            "name": "List_of_Harmonics_Pitch",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_harmonics_roll: Optional[ListOfHarmonicsType] = field(
        default=None,
        metadata={
            "name": "List_of_Harmonics_Roll",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_harmonics_yaw: Optional[ListOfHarmonicsType] = field(
        default=None,
        metadata={
            "name": "List_of_Harmonics_Yaw",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
