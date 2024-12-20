"""
gpt_adapter.py
Adapter for interacting with OpenAI GPT models.
"""
import os
import sys
from typing import List, Dict, Optional
from openai import OpenAI

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from llm_integration.llm_tools import truncate_prompt, construct_chat_prompt, parse_response

#Just a Placeholder for now. Will be updated later
class GPTAdapter:
    def __init__(self, api_key: str, engine: str = "gpt4-large"):
        openai.api_key = api_key
        self.engine = engine
        def generate_response(
        self,
        prompt: str,
        max_tokens: int = 100,
        stop_sequence: Optional[str] = None,
        temperature: float = 0.7,
        n: int = 1,
        logprobs: int = 10,
        presence_penalty: float = 0.0,
        frequency_penalty: float = 0.0,
        best_of: int = 1,
        echo: bool = False,
    ) -> List[Dict[str, str]]:
            
            prompt = truncate_prompt(prompt, max_tokens)
            prompt = construct_chat_prompt(prompt, stop_sequence)
            response = openai.Completion.create(
                engine=self.engine,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                n=n,
                logprobs=logprobs,
                presence_penalty=presence_penalty,
                frequency_penalty=frequency_penalty,
                best_of=best_of,
                echo=echo,
            )
            return parse_response(response)
        
 