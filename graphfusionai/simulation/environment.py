import numpy as np

class SimulationEnvironment:
    def __init__(self, name: str, size=(10, 10)):
        self.name = name
        self.size = size
        self.grid = np.zeros(size)  # Initialize a 2D grid
        self.agents = []           # List of agents in the environment

    def add_agent(self, agent):
        """Add an agent to the simulation."""
        self.agents.append(agent)

    def step(self):
        """Perform one step in the simulation."""
        for agent in self.agents:
            agent.act(self)  # Assume agents have an `act` method
            print(f"Agent {agent.name} acted.")

    def reset(self):
        """Reset the environment."""
        self.grid.fill(0)
        self.agents.clear()

    def render(self):
        """Display the grid as ASCII or pass to a visualizer."""
        print(self.grid)
