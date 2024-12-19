# graphfusionai/core/dynamicmemory_cell.py
import torch
import torch.nn as nn
from typing import Optional, Tuple

class DynamicMemoryCell(nn.Module):
    def __init__(self, input_dim: int, memory_dim: int, context_dim: int):
        super().__init__()
        self.context_layer = nn.MultiheadAttention(embed_dim=context_dim, num_heads=4)
        self.memory_update = nn.GRUCell(input_size=input_dim, hidden_size=memory_dim)
        self.input_projection = nn.Linear(input_dim, context_dim)
        self.memory_projection = nn.Linear(memory_dim, context_dim)
        
        # Additional components for enhanced memory operations
        self.forget_gate = nn.Linear(memory_dim + input_dim, memory_dim)
        self.output_gate = nn.Linear(memory_dim, memory_dim)
        
    def forward(self, 
                input_tensor: torch.Tensor,
                previous_memory: torch.Tensor,
                context: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, torch.Tensor]:
        
        projected_input = self.input_projection(input_tensor)
        projected_memory = self.memory_projection(previous_memory)

        if context is None:
            context = projected_input

        # Apply attention mechanism
        context_aware_input, attention_weights = self.context_layer(
            projected_input.unsqueeze(0),
            projected_memory.unsqueeze(0),
            context.unsqueeze(0)
        )

        # Apply forget gate
        forget_input = torch.cat([previous_memory, input_tensor], dim=-1)
        forget_gate = torch.sigmoid(self.forget_gate(forget_input))
        gated_memory = previous_memory * forget_gate

        # Update memory with context-aware input
        updated_memory = self.memory_update(
            context_aware_input.squeeze(0),
            gated_memory
        )

        # Apply output gate
        output_gate = torch.sigmoid(self.output_gate(updated_memory))
        gated_output = updated_memory * output_gate

        return gated_output, attention_weights

    def reset_memory(self, batch_size: int = 1) -> torch.Tensor:
        device = next(self.parameters()).device
        return torch.zeros(batch_size, self.memory_update.hidden_size, device=device)