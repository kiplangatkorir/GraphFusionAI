# graphfusionai/agents/worker_agent.py
import torch
import torch.nn as nn
from .base_agent import BaseAgent

class WorkerAgent(BaseAgent):
    def __init__(self, input_dim, memory_dim, context_dim, action_dim):
        super().__init__(input_dim, memory_dim, context_dim)
        
        self.action_net = nn.Sequential(
            nn.Linear(memory_dim, memory_dim),
            nn.ReLU(),
            nn.Linear(memory_dim, action_dim),
            nn.Tanh()  # or other activation depending on action space
        )
        
    def decide_action(self, state):
        return self.action_net(state)

    def update(self, reward):
        # Implement learning logic here
        pass