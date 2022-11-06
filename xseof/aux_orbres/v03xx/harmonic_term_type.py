from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class HarmonicTermType:
    class Meta:
        name = "Harmonic_Term_Type"

    reference_time: Optional["HarmonicTermType.ReferenceTime"] = field(
        default=None,
        metadata={
            "name": "Reference_Time",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    period: Optional["HarmonicTermType.Period"] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    amplitude_sin: Optional["HarmonicTermType.AmplitudeSin"] = field(
        default=None,
        metadata={
            "name": "Amplitude_Sin",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    amplitude_cos: Optional["HarmonicTermType.AmplitudeCos"] = field(
        default=None,
        metadata={
            "name": "Amplitude_Cos",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    seq: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class ReferenceTime:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r"(\d{4}-(((01|03|05|07|08|10|12)-(0[1-9]|[1,2][0-9]|3[0,1]))|((04|06|09|11)-(0[1-9]|[1,2][0-9]|30))|(02-(0[1-9]|[1,2][0-9])))T([0,1][0-9]|2[0-3])(:[0-5][0-9]){2}|0000-00-00T00:00:00|9999-99-99T99:99:99)(.\d*)?",
            }
        )
        time_ref: str = field(
            init=False,
            default="UT1",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Period:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="day",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AmplitudeSin:
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
    class AmplitudeCos:
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
