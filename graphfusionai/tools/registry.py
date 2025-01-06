from typing import Dict, Type

# Registry for tools
class ToolRegistry:
    _tools: Dict[str, Type] = {}

    @classmethod
    def register_tool(cls, name: str, tool_class: Type) -> None:
        """
        Register a tool by its name.
        """
        cls._tools[name] = tool_class

    @classmethod
    def get_tool(cls, name: str):
        """
        Retrieve a tool by its name.
        """
        if name not in cls._tools:
            raise ValueError(f"Tool '{name}' not registered.")
        return cls._tools[name]

    @classmethod
    def list_tools(cls):
        """
        List all available tools.
        """
        return list(cls._tools.keys())