import torch
import torch.nn as nn
import networkx as nx
from typing import Dict, Any, Optional, List

class GraphNode:
    def __init__(self, 
                 node_id: str, 
                 features: Optional[Dict[str, Any]] = None,
                 node_type: Optional[str] = None):
        self.node_id = node_id
        self.features = features if features is not None else {}
        self.node_type = node_type
        self.state = None
        self.neighbors: Dict[str, List['GraphNode']] = {
            'in': [],
            'out': []
        }

    def add_neighbor(self, node: 'GraphNode', direction: str = 'out'):
        if direction in ['in', 'out']:
            if node not in self.neighbors[direction]:
                self.neighbors[direction].append(node)

class GraphNetwork(nn.Module):
    def __init__(self, feature_dim: int, hidden_dim: int):
        super().__init__()
        self.graph = nx.DiGraph()
        self.feature_dim = feature_dim
        self.hidden_dim = hidden_dim
        
        self.node_update = nn.GRUCell(feature_dim, hidden_dim)
        self.message_net = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.attention = nn.MultiheadAttention(hidden_dim, num_heads=4)
        
        self.nodes: Dict[str, GraphNode] = {}
        self.node_states: Dict[str, torch.Tensor] = {}

    def add_node(self, 
                 node_id: str, 
                 features: Optional[Dict[str, Any]] = None,
                 node_type: Optional[str] = None) -> GraphNode:
        node = GraphNode(node_id, features, node_type)
        self.nodes[node_id] = node
        self.graph.add_node(node_id, node=node)
        self.node_states[node_id] = torch.zeros(self.hidden_dim)
        return node

    def add_edge(self, 
                 from_node: str, 
                 to_node: str, 
                 edge_type: Optional[str] = None) -> None:
        self.graph.add_edge(from_node, to_node, type=edge_type)
        self.nodes[from_node].add_neighbor(self.nodes[to_node], 'out')
        self.nodes[to_node].add_neighbor(self.nodes[from_node], 'in')

    def message_passing(self) -> Dict[str, torch.Tensor]:
        new_states = {}
        for node_id, node in self.nodes.items():
            in_neighbors = list(self.graph.predecessors(node_id))
            if not in_neighbors:
                new_states[node_id] = self.node_states[node_id]
                continue

            neighbor_states = torch.stack([self.node_states[n] for n in in_neighbors])
            query = self.node_states[node_id].unsqueeze(0).unsqueeze(0)
            key = value = neighbor_states.unsqueeze(0)

            attended_states, _ = self.attention(query, key, value)
            attended_states = attended_states.squeeze(0).squeeze(0)

            new_states[node_id] = self.node_update(
                attended_states,
                self.node_states[node_id]
            )

        self.node_states = new_states
        return new_states

    def forward(self, node_inputs: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        for node_id, input_tensor in node_inputs.items():
            if node_id in self.node_states:
                self.node_states[node_id] = self.node_update(
                    input_tensor,
                    self.node_states[node_id]
                )

        return self.message_passing()