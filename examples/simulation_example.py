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
        # Dummy action: move randomly
        self.position = (self.position[0] + 1, self.position[1] + 1)

# Initialize environment
env = SimulationEnvironment(name="Test Environment", size=(5, 5))
agent1 = DummyAgent(name="Agent1", position=(0, 0))
env.add_agent(agent1)

# Simulate a few steps
env.step()
env.render()

# Visualize
visualizer = SimulationVisualizer(env)
visualizer.visualize_grid()
visualizer.plot_agent_positions()
