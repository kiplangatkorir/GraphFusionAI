from .base_agent import BaseAgent
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMReasoningAgent(BaseAgent):
    def __init__(self, name: str, graph_network, knowledge_graph, llm_model_name: str = "gpt-3.5-turbo"):
        super().__init__(name, graph_network, knowledge_graph)
        self.llm_model_name = llm_model_name
        self.tokenizer = AutoTokenizer.from_pretrained(llm_model_name)
        self.model = AutoModelForCausalLM.from_pretrained(llm_model_name)

    def process_input(self, input_data: str) -> str:
        """
        Use an LLM to process and understand the input data.
        """
        inputs = self.tokenizer.encode(input_data, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50, num_return_sequences=1)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"[LLM Agent {self.name}] Processed Input: {result}")
        return result

    def reason(self, context_data: str) -> str:
        """
        Perform reasoning based on provided context.
        """
        query = f"Based on the following information, make a decision:\n{context_data}"
        result = self.process_input(query)
        print(f"[LLM Agent {self.name}] Reasoning Result: {result}")
        return result

    def decide(self, input_data: str) -> str:
        """
        Make decisions using LLM-based reasoning.
        """
        print(f"[LLM Agent {self.name}] Making decision...")
        return self.reason(input_data)
