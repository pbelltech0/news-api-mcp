import requests
import os
from urllib import parse
from enum import Enum

API_KEY = os.getenv("NEWS_API_KEY", "")


class Endpoint(Enum):
    EVERYTHING = "everything"
    TOP_HEADLINES = "top-headlines"


class NewsAPI:
    def __init__(self):
        return

    def get_top_headlines(
        self,
        query=None,
        country=None,
        category=None,
        sources=None,
        page_size=None,
        page=None,
    ):
        base_url = "https://newsapi.org/v2/top-headlines"
        params = {}
        if query:
            params["q"] = query
        if country:
            params["country"] = country
        if category:
            params["category"] = category
        if sources:
            params["sources"] = sources
        if page_size:
            # Note: News API uses 'pageSize' (camelCase)
            params["pageSize"] = page_size
        if page:
            params["page"] = page
        params["apiKey"] = API_KEY  # Assuming API_KEY is defined elsewhere

        # TODO: add try/except logic
        query_string = parse.urlencode(params)
        base_url = f"{base_url}?{query_string}"
        response = requests.get(base_url)
        return response.json()

    def get_everything(
        self,
        query=None,
        search_in=None,
        sources=None,
        domains=None,
        exclude_domains=None,
        from_date=None,
        to_date=None,
        language=None,
        sortBy=None,
        pageSize=None,
        page=None,
    ):
        base_url = "https://newsapi.org/v2/everything"

        params = {}
        if query:
            params["q"] = query
        if search_in:
            # Note: News API uses 'pageSize' (camelCase)
            params["searchIn"] = search_in
        if sources:
            params["sources"] = sources
        if domains:
            params["domains"] = domains
        if exclude_domains:
            params["exclude_domains"] = exclude_domains
        if from_date:
            params["from_date"] = from_date
        if to_date:
            params["to_date"] = to_date
        if language:
            params["language"] = language
        if sortBy:
            params["sortBy"] = sortBy
        if pageSize:
            params["pageSize"] = pageSize
        if page:
            params["page"] = page
        params["apiKey"] = API_KEY  # Assuming API_KEY is defined elsewhere

        # TODO: add try/except logic
        query_string = parse.urlencode(params)
        base_url = f"{base_url}?{query_string}"
        response = requests.get(base_url)
        return response.json()
