import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphfusionai.core.graph import GraphNetwork
from graphfusionai.core.knowledge_graph import KnowledgeGraph
from graphfusionai.agents import LLMReasoningAgent

# Initialize the graph network and knowledge graph
graph_net = GraphNetwork(feature_dim=128, hidden_dim=256)
knowledge_graph = KnowledgeGraph(entity_dim=128, relation_dim=64)

# Create an LLM Reasoning Agent using Hugging Face
llm_agent = LLMReasoningAgent(
    name="Reasoner", 
    graph_network=graph_net, 
    knowledge_graph=knowledge_graph,
    model_name="gpt2"  # Choose an open-source model
)

# Simulate a reasoning task
context = "Our sales are declining in the European region due to increased competition. How should we respond?"
decision = llm_agent.decide(context)
print(f"LLM Agent's Decision: {decision}")
