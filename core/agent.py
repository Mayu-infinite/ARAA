from abc import ABC, abstractmethod
from typing import Any

class Agent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, state) -> Any:
        """
        Execute agent logic using shared state.
        Must return output.
        Must NOT control the flow.
        """
        pass
