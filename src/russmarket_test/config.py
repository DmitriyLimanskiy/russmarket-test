import os

from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "qwen-local")
model_url = os.getenv("MODEL_URL", "127.0.0.1:8080")
apikey = os.getenv("APIKEY", "local")
