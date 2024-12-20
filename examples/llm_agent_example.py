# llm_agent_example.py

import os
import sys

# Adjust path for local imports (ensure examples can locate the project structure)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphfusionai.core.graph import GraphNetwork
from graphfusionai.core.knowledge_graph import KnowledgeGraph
from graphfusionai.agents.llm_reasoning_agent import LLMReasoningAgent
from graphfusionai.simulation import SimulationEnvironment, SimulationVisualizer

def main():
    # Initialize a simulation environment
    env = SimulationEnvironment(name="LLM-Agent-Demo", size=(5, 5))

    # Create and initialize the knowledge graph and graph network
    graph_network = GraphNetwork(feature_dim=128, hidden_dim=256)
    knowledge_graph = KnowledgeGraph(entity_dim=128, relation_dim=64)

    # Set up the LLM-backed reasoning agent (using Hugging Face Transformers)
    llm_agent = LLMReasoningAgent(
        name="Strategist",
        graph_network=graph_network,
        knowledge_graph=knowledge_graph,
        model_name="gpt2"  # Open-source LLM
    )

    # Add the agent to the environment
    env.add_agent(llm_agent)

    # Define the context for reasoning
    context = (
        "Sales in the European region are declining due to increased competition. "
        "Identify strategies to respond and suggest a course of action."
    )

    # Use the agent to simulate a decision-making scenario
    decision = llm_agent.decide(context)
    print("\n--- Simulation Results ---")
    print(f"Context:\n{context}")
    print(f"LLM Agent's Decision:\n{decision}")

    # Render environment state (for demonstration purposes)
    env.render()

    # Optional: Visualize with the simulation visualizer
    visualizer = SimulationVisualizer(env)
    visualizer.visualize_grid()

if __name__ == "__main__":
    main()
