from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class AngleType:
    class Meta:
        name = "Angle_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="deg",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AnyTypeType:
    class Meta:
        name = "AnyType_Type"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class DistanceType:
    class Meta:
        name = "Distance_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="m",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FreqType:
    class Meta:
        name = "Freq_Type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: str = field(
        init=False,
        default="MHz",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class RefractionModelType(Enum):
    NO_REF = "NO_REF"
    STD_REF = "STD_REF"
    USER_REF = "USER_REF"
    PRED_REF = "PRED_REF"


@dataclass
class Declination(AngleType):
    pass


@dataclass
class HeightType(DistanceType):
    class Meta:
        name = "Height_Type"


@dataclass
class RefractionType:
    class Meta:
        name = "Refraction_Type"

    model: Optional[RefractionModelType] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    freq: Optional[FreqType] = field(
        default=None,
        metadata={
            "name": "Freq",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )


@dataclass
class RightAsc(AngleType):
    class Meta:
        name = "Right_Asc"
