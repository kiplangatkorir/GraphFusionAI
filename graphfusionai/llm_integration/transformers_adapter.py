from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class TransformersAdapter:
    def __init__(self, model_name: str = "gpt2"):
        """
        Adapter for Hugging Face Transformers models.
        """
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def query(self, prompt: str, max_length: int = 150) -> str:
        """
        Query the Hugging Face model with a prompt.
        """
        try:
            inputs = self.tokenizer.encode(prompt, return_tensors="pt")
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                num_return_sequences=1,
                temperature=0.7
            )
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Error querying Transformers model: {e}")
            return "Error occurred while querying the model."
