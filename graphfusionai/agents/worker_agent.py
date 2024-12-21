from .base_agent import BaseAgent

class WorkerAgent(BaseAgent):
    def __init__(self, name, graph_network, knowledge_graph, action_dim):
        super().__init__(name, graph_network, knowledge_graph)  # Initialize BaseAgent
        self.action_dim = action_dim  # New attribute for WorkerAgent

    def process_input(self, input_data: str) -> None:
        """
        Processes specific tasks using the provided data.
        """
        print(f"[Worker {self.name}] Processing input: {input_data}")
    
    def decide(self, input_data: str) -> str:
        """
        Simple decision-making for task-specific actions.
        """
        print(f"[Worker {self.name}] Deciding next action for: {input_data}")
        return f"Action based on {input_data}"
    
    def communicate(self, other_agent: "BaseAgent", message: str) -> None:
        """
        Communicates with another agent.
        """
        print(f"[Worker {self.name}] Sending message to {other_agent.name}: {message}")
    def complete_task(self):
        self.is_available = True
        print(f"[{self.name}] Task completed and ready for new task!")
