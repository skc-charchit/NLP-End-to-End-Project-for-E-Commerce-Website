import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class NewsAPIClient:
    def __init__(self):
        self.base_url = "https://news-api14.p.rapidapi.com/v2"
        self.api_key = os.getenv("RAPIDAPI_KEY")
        self.api_host = "news-api14.p.rapidapi.com"
        self.headers = {
            "x-rapidapi-host": self.api_host,
            "x-rapidapi-key": self.api_key
        }

    def fetch_publishers(self, query="news"):
        """Fetch list of news publishers"""
        url = f"{self.base_url}/search/publishers"
        params = {"query": query}  # <-- required query param
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch publishers. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
