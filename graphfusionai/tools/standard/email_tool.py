import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from graphfusionai.tools.base import BaseTool
from graphfusionai.tools.registry import ToolRegistry

class EmailTool(BaseTool):
    def __init__(self):
        super().__init__()
    
    def execute(self, recipient: str, subject: str, message: str) -> str:
        """
        Executes the email sending task.
        
        Args:
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            message (str): The body content of the email.
        
        Returns:
            str: A success or failure message.
        """
        
        sender_email = "korirkiplangat22@gmail.com"  # Replace with the actual sender email
        sender_password = "K0rir@2020!"  # Replace with your actual sender email password
        smtp_server = "smtp.gmail.com"  # Example for Gmail
        smtp_port = 587
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, recipient, text)
            return f"Email sent successfully to {recipient}!"
        except Exception as e:
            return f"Failed to send email to {recipient}. Error: {str(e)}"

from graphfusionai.tools.registry import ToolRegistry
ToolRegistry.register_tool("email", EmailTool)
