from dataclasses import dataclass, field
from typing import Optional
from .orbit_scenario_variable_header_time_reference import OrbitScenarioVariableHeaderTimeReference

__NAMESPACE__ = "http://eop-cfi.esa.int/CFI"


@dataclass
class OrbitScenarioVariableHeader:
    class Meta:
        name = "Orbit_Scenario_Variable_Header"

    time_reference: Optional[OrbitScenarioVariableHeaderTimeReference] = field(
        default=None,
        metadata={
            "name": "Time_Reference",
            "type": "Element",
            "namespace": "http://eop-cfi.esa.int/CFI",
            "required": True,
        }
    )
