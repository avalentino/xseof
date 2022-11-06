from dataclasses import dataclass, field
from typing import Optional
from .orbit_information_type import OrbitInformationType
from .product_confidence_data_type import ProductConfidenceDataType
from .product_location_type import ProductLocationType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class SphType:
    class Meta:
        name = "SPH_Type"

    sph_descriptor: Optional[str] = field(
        default=None,
        metadata={
            "name": "SPH_Descriptor",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    orbit_information: Optional[OrbitInformationType] = field(
        default=None,
        metadata={
            "name": "Orbit_Information",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    product_location: Optional[ProductLocationType] = field(
        default=None,
        metadata={
            "name": "Product_Location",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    product_confidence_data: Optional[ProductConfidenceDataType] = field(
        default=None,
        metadata={
            "name": "Product_Confidence_Data",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
