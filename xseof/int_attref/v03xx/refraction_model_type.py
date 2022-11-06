from enum import Enum

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


class RefractionModelType(Enum):
    NO_REF = "NO_REF"
    STD_REF = "STD_REF"
    USER_REF = "USER_REF"
    PRED_REF = "PRED_REF"
