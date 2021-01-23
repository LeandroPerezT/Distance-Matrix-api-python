import requests
import json
from urllib.parse import urlencode

api_key = 'your api key'
destiny = "La Plata, Buenos Aires"
origin = "Concepcion, Tucuman"


def get_distance_matrix_for(destiny, origin, api_key):
    
    data_type = 'json'
    endpoint = f"https://api.distancematrix.ai/maps/api/distancematrix/{data_type}"
    params = {"origins": origin, "destinations": destiny, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    api_response = requests.get(url)
    data = api_response.json()

    return data


def get_formated_distance(data):
    
    distance = ''
    for rows in data['rows']:
        distance = rows['elements'][0]['distance']['text']
    return distance


def get_formated_time_travel(data):
    
    duration = ''
    for rows in data['rows']:
        duration = rows['elements'][0]['duration']['text']
    return duration




def get_distance_value(data):
    
    distance = ''
    for rows in data['rows']:
        distance = rows['elements'][0]['distance']['value']
    return distance/1000



def get_time_value(data):
    distance = ''
    for rows in data['rows']:
        distance = rows['elements'][0]['distance']['value']
    return distance
