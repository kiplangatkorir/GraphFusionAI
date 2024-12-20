# examples/simple_agent_workflow.py
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import torch
from graphfusionai.agents import WorkerAgent, ManagerAgent
from graphfusionai.core import GraphNetwork

def main():
    # Initialize dimensions
    input_dim = 64
    memory_dim = 128
    context_dim = 96
    action_dim = 32
    n_workers = 4

    # Create graph network
    graph = GraphNetwork(feature_dim=input_dim, hidden_dim=memory_dim)

    # Create manager agent
    manager = ManagerAgent(input_dim, memory_dim, context_dim, n_workers)

    # Create worker agents
    workers = [
        WorkerAgent(input_dim, memory_dim, context_dim, action_dim)
        for _ in range(n_workers)
    ]

    # Add agents to graph
    manager_node = graph.add_node("manager")
    worker_nodes = []
    for i, worker in enumerate(workers):
        worker_node = graph.add_node(f"worker_{i}")
        worker_nodes.append(worker_node)
        graph.add_edge("manager", f"worker_{i}", edge_type="manages")

    # Simulation loop
    for step in range(100):
        # Generate some observation
        observation = torch.randn(input_dim)

        # Manager processes observation and assigns tasks
        manager_state, _ = manager.process_observation(observation)
        task_assignments = manager.decide_action(manager_state)

        # Workers process their assigned tasks
        worker_states = []
        worker_actions = []
        for worker, assignment in zip(workers, task_assignments):
            worker_obs = torch.cat([observation, assignment.unsqueeze(0)])
            worker_state, _ = worker.process_observation(worker_obs)
            worker_states.append(worker_state)
            action = worker.decide_action(worker_state)
            worker_actions.append(action)

        # Manager processes worker states
        attended_states, attention = manager.process_worker_states(worker_states)

        # Here you would implement environment interaction and rewards

if __name__ == "__main__":
    main()