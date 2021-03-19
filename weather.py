from datetime import datetime
import os
import pytz
import math 
import requests

API_KEY = 'c743d5a22a28f737d0c0d8ae136d957b'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric')

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        response = requests.get(API_URL.format(city, API_KEY))
        return response.json()
    except Exception as exc:
        print(exc)
        data = None
        return data
        