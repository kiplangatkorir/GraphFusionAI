from .base_agent import BaseAgent
from typing import List

class ManagerAgent(BaseAgent):
    def __init__(self, name: str, graph_network, knowledge_graph, worker_agents: List[BaseAgent]):
        super().__init__(name, graph_network, knowledge_graph)
        self.worker_agents = worker_agents

    def assign_task(self, task: str, worker_name: str) -> None:
        """
        Assigns tasks to worker agents by their names.
        """
        for agent in self.worker_agents:
            if agent.name == worker_name:
                print(f"[Manager {self.name}] Assigning task '{task}' to Worker {worker_name}")
                agent.process_input(task)

    def decide(self, input_data: str) -> str:
        """
        Manager-level decision-making based on input data.
        """
        print(f"[Manager {self.name}] High-level decision-making for: {input_data}")
        return f"Plan of action based on {input_data}"
