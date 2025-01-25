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
        
        sender_email = "youremail@example.com"  # Replace with your actual sender email
        sender_password = "yourpassword"  # Replace with your actual sender email password
        smtp_server = "smtp.gmail.com"  # Example for Gmail
        smtp_port = 587
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        try:
            # Connect to SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, recipient, text)
            return f"Email sent successfully to {recipient}!"
        except Exception as e:
            return f"Failed to send email to {recipient}. Error: {str(e)}"

# Register the tool
from graphfusionai.tools.registry import ToolRegistry
ToolRegistry.register_tool("email", EmailTool)
