from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Workflow:
    name: str
    on: On
    jobs: List[Job]
    permissions: Optional[Dict[str, str]] = None
    env: Optional[Dict[str, str]] = None

    def to_dict(self):
        result = {
            "name": self.name,
            "on": self.on.to_dict(),
            "jobs": {job.id: job.to_dict() for job in self.jobs},
        }
        additional_attrs = {k: v for k, v in vars(self).items() if v is not None and k not in result}
        result.update(additional_attrs)
        return result