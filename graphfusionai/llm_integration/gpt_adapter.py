"""
gpt_adapter.py
Adapter for interacting with OpenAI GPT models.
"""

import openai
from typing import List, Dict, Optional
from llm_integration.llm_tools import truncate_prompt, construct_chat_prompt, parse_response


class GPTAdapter:
    """
    Adapter for handling interactions with OpenAI GPT models.
    """

    def __init__(self, api_key: str, model: str = "gpt-4", max_tokens: int = 4096):
        """
        Initialize the GPTAdapter.

        Args:
            api_key (str): OpenAI API key.
            model (str): Model to use (default: "gpt-4").
            max_tokens (int): Maximum token limit for requests (default: 4096).
        """
        openai.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens

    def send_prompt(
        self,
        prompt: str,
        temperature: float = 0.7,
        top_p: float = 1.0,
        max_response_tokens: int = 512
    ) -> Optional[str]:
        """
        Send a text-based prompt to the GPT model.

        Args:
            prompt (str): The input prompt.
            temperature (float): Sampling temperature for response randomness (default: 0.7).
            top_p (float): Probability threshold for nucleus sampling (default: 1.0).
            max_response_tokens (int): Maximum tokens for the response (default: 512).

        Returns:
            Optional[str]: The response content, or None if the request fails.
        """
        truncated_prompt = truncate_prompt(prompt, self.max_tokens - max_response_tokens)
        
        try:
            response = openai.Completion.create(
                model=self.model,
                prompt=truncated_prompt,
                temperature=temperature,
                top_p=top_p,
                max_tokens=max_response_tokens,
                n=1
            )
            return response["choices"][0]["text"].strip()
        except Exception as e:
            print(f"Error during GPT request: {e}")
            return None

    def send_chat(
        self,
        chat_history: List[Dict[str, str]],
        temperature: float = 0.7,
        top_p: float = 1.0,
        max_response_tokens: int = 512
    ) -> Optional[str]:
        """
        Send a conversation-style input to the GPT model.

        Args:
            chat_history (List[Dict[str, str]]): The conversation history as a list of dictionaries.
            temperature (float): Sampling temperature for response randomness (default: 0.7).
            top_p (float): Probability threshold for nucleus sampling (default: 1.0).
            max_response_tokens (int): Maximum tokens for the response (default: 512).

        Returns:
            Optional[str]: The assistant's response content, or None if the request fails.
        """
        formatted_history = construct_chat_prompt(chat_history)
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=formatted_history,
                temperature=temperature,
                top_p=top_p,
                max_tokens=max_response_tokens,
                n=1
            )
            return parse_response(response)
        except Exception as e:
            print(f"Error during GPT chat request: {e}")
            return None
