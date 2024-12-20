import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from graphfusionai.simulation import SimulationEnvironment
from graphfusionai.simulation import SimulationVisualizer

class DummyAgent:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def act(self, environment):
        # Dummy action: Move randomly within bounds
        new_x = min(self.position[0] + 1, environment.size[0] - 1)
        new_y = min(self.position[1] + 1, environment.size[1] - 1)
        self.position = (new_x, new_y)
        environment.update_agent_position(self)

# Initialize environment
env = SimulationEnvironment(name="Test Environment", size=(5, 5))
agent1 = DummyAgent(name="Agent1", position=(0, 0))
agent2 = DummyAgent(name="Agent2", position=(4, 4))  # Start at a different location
env.add_agent(agent1)
env.add_agent(agent2)

# Simulate steps
for step in range(3):  # Simulate 3 steps
    print(f"\nStep {step + 1}:")
    env.step()
    env.render()

# Visualize
visualizer = SimulationVisualizer(env)
visualizer.visualize_grid()  # Show grid as a visual graph
visualizer.plot_agent_positions()  # Plot agents on a chart
