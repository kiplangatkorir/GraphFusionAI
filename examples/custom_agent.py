import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphfusionai.builder import AgentBuilder
from graphfusionai.agents.support_agent import SupportAgent
from graphfusionai.core.graph import GraphNetwork
from graphfusionai.core.knowledge_graph import KnowledgeGraph

# Define dimensions
feature_dim = 128      
hidden_dim = 256       
entity_dim = 64       
relation_dim = 32       

graph_network = GraphNetwork(feature_dim=feature_dim, hidden_dim=hidden_dim)
knowledge_graph = KnowledgeGraph(entity_dim=entity_dim, relation_dim=relation_dim)

config = {
    "memory": {
        "input_dim": 128,
        "memory_dim": 256,
        "context_dim": 64
    },
    "tools": ["email", "web"]
}

builder = AgentBuilder(graph_network, knowledge_graph)
agent = builder.create_agent(SupportAgent, "CustomerSupportAgent", config)

# Validate tool integration
print(agent.tools)  # Should display the attached tool objects.
