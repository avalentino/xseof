from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from ..common.basic_types_0101 import AngleType
from ..common.time_types_0102 import TimeReferenceType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class MaxGapType:
    class Meta:
        name = "Max_Gap_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="s",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AngleTimeType:
    class Meta:
        name = "Angle_Time_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[A-Z0-9]{3}=(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}|0000-00-00T00:00:00|9999-99-99T99:99:99)(.\d*)?",
        }
    )
    ref: Optional[TimeReferenceType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AnglesDataType:
    class Meta:
        name = "Angles_Data_Type"

    time: Optional[AngleTimeType] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    pitch: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Pitch",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    roll: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Roll",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    yaw: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "Yaw",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class QuaternionType:
    class Meta:
        name = "Quaternion_Type"

    time: Optional[AngleTimeType] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    q1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Q1",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    q2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Q2",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    q3: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Q3",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    q4: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Q4",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class ListOfAttitudeAnglesType:
    class Meta:
        name = "List_of_Attitude_Angles_Type"

    attitude_angles: List[AnglesDataType] = field(
        default_factory=list,
        metadata={
            "name": "Attitude_Angles",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "min_occurs": 1,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ListOfQuaternionsType:
    class Meta:
        name = "List_of_Quaternions_Type"

    quaternions: List[QuaternionType] = field(
        default_factory=list,
        metadata={
            "name": "Quaternions",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "min_occurs": 1,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AttitudeAnglesDataType:
    class Meta:
        name = "Attitude_Angles_Data_Type"

    list_of_attitude_angles: Optional[ListOfAttitudeAnglesType] = field(
        default=None,
        metadata={
            "name": "List_of_Attitude_Angles",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class QuaternionDataType:
    class Meta:
        name = "Quaternion_Data_Type"

    inertial_ref_frame: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inertial_Ref_Frame",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_quaternions: Optional[ListOfQuaternionsType] = field(
        default=None,
        metadata={
            "name": "List_of_Quaternions",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


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


@dataclass
class DataBlock(AttitudeDataBlockType):
    class Meta:
        name = "Data_Block"
        namespace = "http://eop-cfi.esa.int/CFI"
