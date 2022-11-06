from dataclasses import dataclass, field
from typing import Optional
from .list_of_files_type import ListOfFilesType
from .time_selection_type import TimeSelectionType

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class FileModel2Type:
    class Meta:
        name = "File_Model2_Type"

    list_of_files: Optional[ListOfFilesType] = field(
        default=None,
        metadata={
            "name": "List_of_Files",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
    time_selection: Optional[TimeSelectionType] = field(
        default=None,
        metadata={
            "name": "Time_Selection",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
