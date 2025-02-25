import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

class Config:
    # Replace these values with your actual credentials in your .env file.
    BAP_ID = os.getenv("BAP_ID", "agripilot.ai")
    BAP_URI = os.getenv("BAP_URI", "https://agripilot.ai/api")
