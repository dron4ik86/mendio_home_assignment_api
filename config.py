import requests
import os
from dotenv import load_dotenv


load_dotenv()
SESSION = requests.Session()
WORKSPACE_TOKEN = os.getenv("WORKSPACE_TOKEN")

