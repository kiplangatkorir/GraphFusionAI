# graphfusionai/agents/manager_agent.py
import torch
import torch.nn as nn
from .base_agent import BaseAgent

class ManagerAgent(BaseAgent):
    def __init__(self, input_dim, memory_dim, context_dim, n_workers):
        super().__init__(input_dim, memory_dim, context_dim)
        self.n_workers = n_workers
        
        self.worker_attention = nn.MultiheadAttention(
            embed_dim=memory_dim,
            num_heads=4
        )
        
        self.task_assignment_net = nn.Sequential(
            nn.Linear(memory_dim, memory_dim),
            nn.ReLU(),
            nn.Linear(memory_dim, n_workers)
        )
        
    def process_worker_states(self, worker_states):
        # worker_states: [n_workers, memory_dim]
        worker_states = torch.stack(worker_states)
        
        # Apply attention over worker states
        attended_states, attention_weights = self.worker_attention(
            worker_states.unsqueeze(0),
            worker_states.unsqueeze(0),
            worker_states.unsqueeze(0)
        )
        
        return attended_states.squeeze(0), attention_weights
        
    def decide_action(self, state):
        # Generate task assignments for workers
        task_assignments = self.task_assignment_net(state)
        return torch.softmax(task_assignments, dim=-1)