from dataclasses import dataclass, field

@dataclass
class AgentState:
    task: str
    steps: list = field(default_factory=list)
    status: str = "running"