import matplotlib.pyplot as plt
import numpy as np

class SimulationVisualizer:
    def __init__(self, environment):
        self.environment = environment

    def visualize_grid(self):
        # Convert grid to numeric values for visualization
        grid = self.environment.grid
        numeric_grid = np.zeros_like(grid, dtype=int)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if isinstance(cell, str) and cell.isalpha():
                    numeric_grid[i, j] = ord(cell.upper()) - ord('A') + 1  # Convert 'A' -> 1, 'B' -> 2
                elif cell == '*':  # Overlap indicator
                    numeric_grid[i, j] = -1

        plt.imshow(numeric_grid, cmap='Greys', interpolation='nearest')
        plt.colorbar(label='Agent Indicators (1=A, 2=B, ...)')
        plt.title(f"Visualization of Grid: {self.environment.name}")
        plt.show()

    def plot_agent_positions(self):
        agent_positions = [agent.position for agent in self.environment.agents]
        agent_names = [agent.name for agent in self.environment.agents]
        x, y = zip(*agent_positions)

        plt.scatter(x, y, c='red', label='Agents')
        for i, name in enumerate(agent_names):
            plt.annotate(name, (x[i], y[i]), textcoords="offset points", xytext=(5, 5), ha='center')
        
        plt.xlim(-0.5, self.environment.size[0] - 0.5)
        plt.ylim(-0.5, self.environment.size[1] - 0.5)
        plt.gca().invert_yaxis()
        plt.grid(True)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Agent Positions")
        plt.legend()
        plt.show()
