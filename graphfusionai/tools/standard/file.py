from tools.base import BaseTool
from tools.registry import ToolRegistry

class FileTool(BaseTool):
    """
    Tool for reading and writing files.
    """
    def execute(self, action: str, file_path: str, content: str = None) -> str:
        if action == "read":
            with open(file_path, 'r') as f:
                return f.read()
        elif action == "write":
            with open(file_path, 'w') as f:
                f.write(content)
                return f"File written to {file_path}"
        else:
            raise ValueError("Unsupported action. Use 'read' or 'write'.")

# Register the tool
ToolRegistry.register_tool("file", FileTool)