import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("Vana@123")
BASE_URL = "https://api.openweathermap.org/data/2.5"
CACHE_DIR = "data/cache"
CACHE_DURATION = 600  # seconds