from tools.base import BaseTool
from tools.registry import ToolRegistry

class EmailTool(BaseTool):
    """
    Tool for sending emails.
    """
    def execute(self, recipient: str, subject: str, body: str) -> str:
        # Mock email sending
        return f"Email sent to {recipient} with subject: '{subject}'."

# Register the tool
ToolRegistry.register_tool("email", EmailTool)