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
        return {k: v for k, v in vars(self).items() if v is not None}

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
