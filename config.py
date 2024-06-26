import os
from dotenv import load_dotenv


load_dotenv()
WORKSPACE_TOKEN = os.getenv("WORKSPACE_TOKEN")
BASE_URL = os.getenv("BASE_URL")

