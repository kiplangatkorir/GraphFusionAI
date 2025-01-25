import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphfusionai.tools.registry import ToolRegistry
from graphfusionai.tools.standard.web import WebTool
from graphfusionai.tools.standard.email_tool import EmailTool
from graphfusionai.tools.standard.file import FileTool

# Register tools
ToolRegistry.register_tool("web", WebTool)
ToolRegistry.register_tool("email", EmailTool)
ToolRegistry.register_tool("file", FileTool)

# Access registered tools
web_tool = ToolRegistry.get_tool("web")()
email_tool = ToolRegistry.get_tool("email")()
file_tool = ToolRegistry.get_tool("file")()

# Example usage
web_result = web_tool.execute("https://msingi-ai.github.io/")
print("Web Result:", web_result[:100])  # Print first 100 chars

email_result = email_tool.execute("korirkiplangat22@gmail.com", "Hello", "This is a test email.")
print("Email Result:", email_result)

file_result = file_tool.execute("write", "sample.txt", "Hello, GraphFusion!")
print("File Result:", file_result)

# Read the same file
file_content = file_tool.execute("read", "sample.txt")
print("File Content:", file_content)
