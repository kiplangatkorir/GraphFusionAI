import matplotlib.pyplot as plt
import numpy as np

class SimulationVisualizer:
    def __init__(self, environment):
        self.environment = environment

    def visualize_grid(self):
        """Visualize the grid using matplotlib."""
        grid = self.environment.grid
        plt.imshow(grid, cmap='Greys', interpolation='nearest')
        plt.title(f"Simulation: {self.environment.name}")
        plt.colorbar()
        plt.show()

    def plot_agent_positions(self):
        """Plot agent positions on the grid."""
        grid = np.zeros(self.environment.size)
        for agent in self.environment.agents:
            x, y = agent.position
            grid[x, y] = 1  # Mark the agent's position
        plt.imshow(grid, cmap='Blues', interpolation='nearest')
        plt.title("Agent Positions")
        plt.colorbar()
        plt.show()
