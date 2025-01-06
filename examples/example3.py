import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphfusionai.builder.agent_builder import AgentBuilder
from graphfusionai.agents.base_agent import BaseAgent
from graphfusionai.core.graph import GraphNetwork
from graphfusionai.core.knowledge_graph import KnowledgeGraph

# Initialize shared graph components
graph_network = GraphNetwork()
knowledge_graph = KnowledgeGraph()

# Initialize the AgentBuilder
builder = AgentBuilder(graph_network, knowledge_graph)

# Define configuration for the custom agent
agent_config = {
    "memory": {
        "input_dim": 128,
        "memory_dim": 256,
        "context_dim": 64
    }
}

# Dynamically create an agent
custom_agent = builder.create_agent(BaseAgent, name="custom_support", config=agent_config)
