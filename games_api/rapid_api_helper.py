from django.http import HttpResponse
from django.conf import settings
import requests
import os

api_url = settings.RAPID_API_URL
api_key = settings.RAPID_API_KEY
api_host = settings.RAPID_API_HOST
empty_json_object = {}

headers = {
    'x-rapidapi-host': api_host,
    'x-rapidapi-key': api_key
}

def get_json(endpoint, query=None):
    url = f'{api_url}/{endpoint}'

    if query:
        url = url + f'?{query}'

    response = requests.get(url, headers=headers)
    return get_response_result(response)

def get_response_result(response):
    if response.ok:
        return response.json()
    return empty_json_object