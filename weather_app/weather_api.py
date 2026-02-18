import requests
import json
import os
import time
from pathlib import Path
from weather_app.config import API_KEY, BASE_URL, CACHE_DIR, CACHE_DURATION


class WeatherAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)

    def _get_cache_path(self, city):
        return os.path.join(CACHE_DIR, f"{city.lower()}.json")

    def _is_cache_valid(self, filepath):
        if not os.path.exists(filepath):
            return False
        return time.time() - os.path.getmtime(filepath) < CACHE_DURATION

    def _load_cache(self, filepath):
        with open(filepath, "r") as f:
            return json.load(f)

    def _save_cache(self, filepath, data):
        with open(filepath, "w") as f:
            json.dump(data, f)

    def get_current_weather(self, city):
        cache_path = self._get_cache_path(city)

        if self._is_cache_valid(cache_path):
            print("Using cached data...")
            return self._load_cache(cache_path)

        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            self._save_cache(cache_path, data)
            return data
        else:
            raise Exception("Failed to fetch weather data")