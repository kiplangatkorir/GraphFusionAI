# builder/validators.py

from typing import Dict, Any

def validate_config(config: Dict[str, Any]) -> None:
    """
    Validates the configuration for building agents.

    Args:
        config (Dict[str, Any]): Configuration dictionary.

    Raises:
        ValueError: If a required key is missing or invalid.
    """
    if "memory" not in config:
        raise ValueError("Agent configuration must include a 'memory' key.")
    
    memory_config = config["memory"]
    required_keys = ["input_dim", "memory_dim", "context_dim"]

    for key in required_keys:
        if key not in memory_config:
            raise ValueError(f"Memory configuration is missing required key: {key}")
    
    # Ensure dimensions are positive integers
    for key, value in memory_config.items():
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Memory dimension '{key}' must be a positive integer.")
