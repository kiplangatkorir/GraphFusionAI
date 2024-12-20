"""
llm_tools.py
Utility functions for interacting with LLMs.
"""

from typing import List, Tuple, Dict


def truncate_prompt(prompt: str, max_tokens: int) -> str:
    """
    Truncate a prompt to fit within a specified token limit.
    
    Args:
        prompt (str): The text to truncate.
        max_tokens (int): Maximum number of tokens allowed.

    Returns:
        str: The truncated prompt.
    """
    return prompt[:max_tokens]


def split_prompt(prompt: str, chunk_size: int) -> List[str]:
    """
    Split a long prompt into smaller chunks.

    Args:
        prompt (str): The input text to split.
        chunk_size (int): The size of each chunk in tokens.

    Returns:
        List[str]: A list of prompt chunks.
    """
    return [prompt[i:i + chunk_size] for i in range(0, len(prompt), chunk_size)]


def construct_chat_prompt(history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Construct a chat-compatible prompt from a message history.

    Args:
        history (List[Dict[str, str]]): A list of dictionaries representing the conversation history,
                                        e.g., [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello"}]

    Returns:
        List[Dict[str, str]]: Formatted history suitable for chat-based LLMs.
    """
    return [{"role": entry["role"], "content": entry["content"]} for entry in history]


def parse_response(response: Dict) -> str:
    """
    Parse the response from an LLM and extract the main content.

    Args:
        response (Dict): The response object from the LLM.

    Returns:
        str: Extracted content (if available).
    """
    try:
        return response["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        return "Error: Unable to parse response."


def calculate_token_usage(text: str, token_length: int = 4) -> int:
    """
    Estimate token usage for a given text (basic approximation).

    Args:
        text (str): The text to estimate token count for.
        token_length (int): Average token length (default: 4 characters per token).

    Returns:
        int: Estimated token count.
    """
    return len(text) // token_length


def validate_prompt_length(prompt: str, max_tokens: int) -> bool:
    """
    Validate whether a prompt fits within the token limit.

    Args:
        prompt (str): The input prompt.
        max_tokens (int): The maximum allowable tokens.

    Returns:
        bool: True if the prompt is valid, False otherwise.
    """
    return calculate_token_usage(prompt) <= max_tokens

def parse_response(response) -> str:
    """
    Extract the assistant's message content from a chat response.
    """
    return response["choices"][0]["message"]["content"]

def get_llm_instance(model_name: str, **kwargs):
    """
    Placeholder for loading a specific LLM instance.
    """
    raise NotImplementedError("get_llm_instance is not implemented.")

def load_model(model_name: str, config: dict):
    """
    Placeholder for loading a pre-trained model.
    """
    raise NotImplementedError("load_model is not implemented.")

