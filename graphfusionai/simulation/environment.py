import numpy as np

class SimulationEnvironment:
    def __init__(self, name, size=(5, 5)):
        self.name = name
        self.size = size
        self.grid = [[0 for _ in range(size[1])] for _ in range(size[0])]
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)
        self.update_agent_position(agent)

    def update_agent_position(self, agent):
        # Clear grid and update with new positions
        self.grid = [[0 for _ in range(self.size[1])] for _ in range(self.size[0])]
        for a in self.agents:
            x, y = a.position
            self.grid[x][y] = a.name[0].upper()  # Represent agent by first letter

    def step(self):
        for agent in self.agents:
            agent.act(self)
            print(f"Agent {agent.name} acted.")

    def render(self):
        for row in self.grid:
            print(' '.join(str(cell) if cell != 0 else '.' for cell in row))


