from .base_agent import BaseAgent
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMReasoningAgent(BaseAgent):
    def __init__(self, 
                 name: str, 
                 graph_network, 
                 knowledge_graph, 
                 model_name: str = "bigscience/bloom-560m"):
        """
        Initialize the LLM Reasoning Agent with a Hugging Face model.
        """
        super().__init__(name, graph_network, knowledge_graph)
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def process_input(self, input_data: str) -> str:
        """
        Generate a response from the Hugging Face model based on input data.
        """
        inputs = self.tokenizer.encode(input_data, return_tensors="pt")
        outputs = self.model.generate(
            inputs, 
            max_length=100, 
            num_return_sequences=1, 
            temperature=0.7
        )
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"[LLM Agent {self.name}] Processed Input: {result}")
        return result

    def reason(self, context_data: str) -> str:
        """
        Perform reasoning based on provided context data.
        """
        query = f"Given the context, what actions should we take?\n{context_data}"
        return self.process_input(query)

    def decide(self, input_data: str) -> str:
        """
        Make a decision using reasoning capabilities.
        """
        print(f"[LLM Agent {self.name}] Making a decision...")
        return self.reason(input_data)
