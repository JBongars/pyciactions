from dataclasses import dataclass
from typing import List, Dict, Optional, Union, Any

@dataclass
class Step:
    name: str
    uses: Optional[str] = None
    run: Optional[Union[str, List[str]]] = None
    working_directory: Optional[str] = None
    shell: Optional[str] = None
    with_: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    env: Optional[Dict[str, Any]] = None

    def to_dict(self):
        result = {"name": self.name}
        for attr, value in vars(self).items():
            if value is not None:
                if attr == "with_":
                    result["with"] = value
                else:
                    result[attr] = value
        return result

@dataclass
class Job:
    id: str
    runs_on: str
    steps: List[Step]
    needs: Optional[List[str]] = None
    if_: Optional[str] = None

    def to_dict(self):
        result = {
            "runs-on": self.runs_on,
            "steps": [step.to_dict() for step in self.steps]
        }
        additional_attrs = {k: v for k, v in vars(self).items() if v is not None and k not in result}
        result.update(additional_attrs)
        return result
