from dataclasses import dataclass, field
from typing import Optional
from .list_of_parameters_type import ListOfParametersType
from .param_model_type_model import ParamModelTypeModel

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class ParamModelType:
    class Meta:
        name = "Param_Model_Type"

    model: Optional[ParamModelTypeModel] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    list_of_parameters: Optional[ListOfParametersType] = field(
        default=None,
        metadata={
            "name": "List_of_Parameters",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
