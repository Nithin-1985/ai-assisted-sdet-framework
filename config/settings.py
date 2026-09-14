import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_USERNAME = os.getenv("API_USERNAME")
API_PASSWORD = os.getenv("API_PASSWORD")
BROWSER = os.getenv("BROWSER")


values = {
    "BASE_URL": BASE_URL,
    "API_USERNAME": API_USERNAME,
    "API_PASSWORD": API_PASSWORD,
    "BROWSER": BROWSER,
}

missing = [name for name, value in values.items() if value is None]

if missing:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing)}"
    )