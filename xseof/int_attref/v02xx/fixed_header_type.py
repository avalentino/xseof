from dataclasses import dataclass, field
from typing import Optional
from .source_type import SourceType
from .validity_period_type import ValidityPeriodType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class FixedHeaderType:
    class Meta:
        name = "Fixed_Header_Type"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Name",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"([A-Z0-9_]){3}_([A-Z0-9_]){4}_([A-Z0-9_]){10}_([A-Z0-9_]){1,41}",
        }
    )
    file_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Description",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    mission: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mission",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    file_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Class",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"OPER|OFFL|NRT_|RPRO|STV[0-3]|GSOV|TEST|TD[0-9][0-9]|Routine Operations|Off-Line Processing|near-real-Time Processing|Re-Processing|Satellite Validation Test [0-3]|Ground Segment Overall Validation test|Generated test files|Test Data Set [0-9][0-9]",
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Type",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"[A-Z0-9_]{10}",
        }
    )
    validity_period: Optional[ValidityPeriodType] = field(
        default=None,
        metadata={
            "name": "Validity_Period",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    file_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "File_Version",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    source: Optional[SourceType] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
