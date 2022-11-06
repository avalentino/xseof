from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ValidityPeriodBomEomType:
    class Meta:
        name = "Validity_Period_BOM_EOM_Type"

    validity_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Start",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"UTC=0000-00-00T00:00:00",
        }
    )
    validity_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "Validity_Stop",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
            "pattern": r"UTC=9999-99-99T99:99:99",
        }
    )
