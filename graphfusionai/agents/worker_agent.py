from .base_agent import BaseAgent

class WorkerAgent(BaseAgent):
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
