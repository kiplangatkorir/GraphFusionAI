# graphfusionai/agents/base_agent.py

import abc
from typing import Any, Dict

class BaseAgent(abc.ABC):
    """
    Abstract base class for agents in GraphFusionAI.
    """
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.memory = {}
    
    @abc.abstractmethod
    def act(self, inputs: Dict[str, Any]) -> Any:
        """
        Perform an action based on the provided inputs.
        """
        pass

    def store_memory(self, key: str, value: Any):
        """
        Store information in the agent's memory.
        """
        self.memory[key] = value

    def recall_memory(self, key: str) -> Any:
        """
        Retrieve information from the agent's memory.
        """
        return self.memory.get(key, None)
