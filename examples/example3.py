import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphfusionai.builder.agent_builder import AgentBuilder
from graphfusionai.agents.base_agent import BaseAgent
from graphfusionai.core.graph import GraphNetwork
from graphfusionai.core.knowledge_graph import KnowledgeGraph

# Specify dimensions for GraphNetwork and KnowledgeGraph
feature_dim = 128   # Input feature size for the graph network
hidden_dim = 256    # Hidden feature size for node representations
entity_dim = 128    # Entity embedding size for knowledge graph
relation_dim = 64   # Relation embedding size for knowledge graph

# Initialize the GraphNetwork with required dimensions
graph_network = GraphNetwork(feature_dim=feature_dim, hidden_dim=hidden_dim)

# Initialize the KnowledgeGraph with required dimensions
knowledge_graph = KnowledgeGraph(entity_dim=entity_dim, relation_dim=relation_dim)

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

# Check if the agent was created successfully
print(f"Created agent: {custom_agent.name}")

