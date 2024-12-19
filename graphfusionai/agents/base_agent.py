# graphfusionai/agents/base_agent.py
import torch
import torch.nn as nn
from ..core.graph import GraphNetwork
from ..core.dynamicmemory_cell import DynamicMemoryCell

class BaseAgent(nn.Module):
    def __init__(self, input_dim, memory_dim, context_dim):
        super().__init__()
        self.memory = DynamicMemoryCell(input_dim, memory_dim, context_dim)
        self.state = None
        self.memory_state = torch.zeros(memory_dim)
        
    def process_observation(self, observation):
        # Convert observation to tensor if needed
        if not isinstance(observation, torch.Tensor):
            observation = torch.tensor(observation, dtype=torch.float32)
            
        # Update memory with new observation
        self.memory_state, attention = self.memory(
            observation,
            self.memory_state
        )
        return self.memory_state, attention

    def decide_action(self, state):
        raise NotImplementedError("Subclasses must implement decide_action")

    def act(self, observation):
        state, _ = self.process_observation(observation)
        action = self.decide_action(state)
        return action