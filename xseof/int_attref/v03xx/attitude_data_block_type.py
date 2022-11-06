from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .attitude_angles_data_type import AttitudeAnglesDataType
from .max_gap_type import MaxGapType
from .quaternion_data_type import QuaternionDataType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AttitudeDataBlockType:
    class Meta:
        name = "Attitude_Data_Block_Type"

    attitude_file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Attitude_File_Type",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    attitude_data_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Attitude_Data_Type",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    max_gap: Optional[MaxGapType] = field(
        default=None,
        metadata={
            "name": "Max_Gap",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    attitude_angles_data: Optional[AttitudeAnglesDataType] = field(
        default=None,
        metadata={
            "name": "Attitude_Angles_Data",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    quaternion_data: Optional[QuaternionDataType] = field(
        default=None,
        metadata={
            "name": "Quaternion_Data",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
        }
    )
    type: str = field(
        init=False,
        default="xml",
        metadata={
            "type": "Attribute",
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
