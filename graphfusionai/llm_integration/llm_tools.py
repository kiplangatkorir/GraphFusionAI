from typing import List, Dict

def truncate_text(text: str, max_length: int) -> str:
    """
    Truncate text to a specified maximum length.
    """
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def format_input_for_llm(prompt: str, context: str = "") -> str:
    """
    Format input by combining context and prompt for LLM reasoning.
    """
    return f"Context:\n{context}\n\nPrompt:\n{prompt}"

def extract_key_points(text: str) -> List[str]:
    """
    Extract key points from a response.
    """
    return [line.strip() for line in text.split("\n") if line.strip()]

def validate_response(response: str, required_keywords: List[str] = []) -> bool:
    """
    Validate an LLM response to ensure it contains specific required keywords.
    """
    return all(keyword in response for keyword in required_keywords)
