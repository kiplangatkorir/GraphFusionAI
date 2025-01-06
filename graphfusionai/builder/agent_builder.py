import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Any, Dict, Type, Union
from graphfusionai.agents.base_agent import BaseAgent
from graphfusionai.core.graph import GraphNetwork
from graphfusionai.core.knowledge_graph import KnowledgeGraph
from graphfusionai.core.memory_cell import DynamicMemoryCell
from builder.validators import validate_config

class AgentBuilder:
    """
    A builder for dynamically creating agents based on specifications.
    """

    def __init__(self, graph_network: GraphNetwork, knowledge_graph: KnowledgeGraph):
        """
        Initialize the AgentBuilder with core components.

        Args:
            graph_network (GraphNetwork): The graph network for agent interaction.
            knowledge_graph (KnowledgeGraph): The shared knowledge graph.
        """
        self.graph_network = graph_network
        self.knowledge_graph = knowledge_graph

    def create_agent(self, 
                     agent_type: Type[BaseAgent], 
                     name: str, 
                     config: Dict[str, Any]
                    ) -> Union[BaseAgent, None]:
        """
        Dynamically creates an agent of the specified type.

        Args:
            agent_type (Type[BaseAgent]): The class type for the agent.
            name (str): The agent's name.
            config (Dict[str, Any]): Configuration for the agent.

        Returns:
            BaseAgent: An initialized agent instance.
        
        Raises:
            ValueError: If the configuration is invalid or missing keys.
        """
        # Validate agent configuration
        validate_config(config)

        # Extract memory configuration
        memory_config = config.get("memory", {})
        memory_cell = DynamicMemoryCell(
            input_dim=memory_config.get("input_dim", 256),
            memory_dim=memory_config.get("memory_dim", 512),
            context_dim=memory_config.get("context_dim", 128)
        )

        # Initialize and return the agent instance
        agent = agent_type(
            name=name,
            graph_network=self.graph_network,
            knowledge_graph=self.knowledge_graph
        )
        agent.memory_cell = memory_cell  # Attach custom memory cell

        return agent
