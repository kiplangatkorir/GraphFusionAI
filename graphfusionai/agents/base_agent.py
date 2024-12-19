from typing import Any, Dict, List, Optional
from graphfusionai.core.graph import GraphNetwork
from graphfusionai.core.knowledge_graph import KnowledgeGraph
from graphfusionai.core.dynamicmemory_cell import DynamicMemoryCell
import torch

class BaseAgent:
    def __init__(self, name: str, graph_network: GraphNetwork, knowledge_graph: KnowledgeGraph):
        self.name = name
        self.graph_network = graph_network
        self.knowledge_graph = knowledge_graph
        self.memory_cell = DynamicMemoryCell(
            input_dim=256, memory_dim=512, context_dim=128
        )

    def process_input(self, input_data: Any) -> Dict[str, torch.Tensor]:
        """
        Abstract method to process input data. Must be implemented in derived classes.
        """
        raise NotImplementedError

    def update_graph(self, updates: List[Dict[str, Any]]) -> None:
        """
        Update the knowledge graph based on new information.
        """
        for update in updates:
            self.knowledge_graph.add_relation(
                update['from'], update['to'], update['relation'], update.get('features')
            )

    def decide(self, input_data: Any) -> Any:
        """
        Abstract method for decision-making. Must be implemented in derived classes.
        """
        raise NotImplementedError

    def communicate(self, other_agent: "BaseAgent", message: Any) -> None:
        """
        Abstract method for inter-agent communication.
        """
        raise NotImplementedError
