from dataclasses import dataclass, field
from typing import Optional
from .instr_att_type import InstrAttType
from .sat_att_type import SatAttType
from .sat_nominal_att_type import SatNominalAttType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AttType:
    class Meta:
        name = "ATT_Type"

    sat_nominal_att: Optional[SatNominalAttType] = field(
        default=None,
        metadata={
            "name": "Sat_Nominal_Att",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    sat_att: Optional[SatAttType] = field(
        default=None,
        metadata={
            "name": "Sat_Att",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    instr_att: Optional[InstrAttType] = field(
        default=None,
        metadata={
            "name": "Instr_Att",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
