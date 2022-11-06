from dataclasses import dataclass, field

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class RelTimeAscNodeType:
    class Meta:
        name = "Rel_Time_ASC_Node_Type"

    value: str = field(
        default="",
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
