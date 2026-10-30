import os
from dataclasses import dataclass

@dataclass
class Config:
    model_name: str = "open/gpt-4o-mini"
    max_steps: int = 10


def load_config() -> Config:
    return Config(
        model_name=os.getenv("ECHO_MODEL", "open/gpt-4o-mini"),
        max_steps=int(os.getenv("ECHO_MAX_STEPS", "10")),
    )