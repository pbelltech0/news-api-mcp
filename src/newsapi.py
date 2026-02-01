import requests
import os
from enum import Enum

API_KEY = os.getenv("NEWS_API_KEY", "")

class Endpoint(Enum):
    EVERYTHING = "everything"
    TOP_HEADLINES = "top-headlines"

class NewsAPI:
    def __init__(self) -> None:
        return
    
    def get_top_headlines(self, query_str: str):
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}&pageSize=2"
        response = requests.get(url)
        print(f"response={response}")
        return response.json()

    def get_everything(self, query_str: str):
        url = self.get_request_url(Endpoint.EVERYTHING.value, query_str)
        response = requests.get(url)
        print(f"url={url}")
        print(f"response={response}")
        return response.json()

    def get_request_url(self, service:str, query: str) -> str:
        return f"https://newsapi.org/v2/{service}?q={query}&apiKey={API_KEY}&country=us"