import requests
from tools.base import BaseTool
from tools.registry import ToolRegistry

class WebTool(BaseTool):
    """
    Tool for web-based actions, such as making HTTP requests.
    """
    def execute(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

# Register the tool
ToolRegistry.register_tool("web", WebTool)