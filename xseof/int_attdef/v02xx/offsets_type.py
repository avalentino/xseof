from dataclasses import dataclass, field

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OffsetsType:
    class Meta:
        name = "Offsets_Type"

    offset_x: str = field(
        default="0",
        metadata={
            "name": "Offset_X",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    offset_y: str = field(
        default="0",
        metadata={
            "name": "Offset_Y",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    offset_z: str = field(
        default="0",
        metadata={
            "name": "Offset_Z",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
