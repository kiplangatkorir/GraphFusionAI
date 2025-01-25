import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphfusionai.agents.base_agent import BaseAgent

class SupportAgent(BaseAgent):
    """
    A support agent that uses memory and tools to assist users.
    """
    def __init__(self, name: str, graph_network, knowledge_graph):
        super().__init__(name, graph_network, knowledge_graph)
        self.tools = []  # Initialize an empty list of tools

    def add_tool(self, tool):
        """
        Add a tool to the agent's toolset.
        
        Args:
            tool (BaseTool): An instance of a tool to add.
        """
        self.tools.append(tool)

    def respond(self, query: str) -> str:
        """
        Respond to a user query using knowledge and tools.

        Args:
            query (str): The query to respond to.

        Returns:
            str: The agent's response.
        """
        # Custom response logic for the support agent
        return f"{self.name} responding to query: {query}"
