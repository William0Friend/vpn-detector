import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
IP2PROXY_DB_PATH = os.getenv("IP2PROXY_DB_PATH")
