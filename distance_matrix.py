import requests
import json
from urllib.parse import urlencode

api_key = 'your api key'
destiny = "La Plata, Buenos Aires"
origin = "Concepcion, Tucuman"


def get_distance_matrix_for(destiny, origin, api_key):
    
    """
    This function takes as parameters your destiny, origin and api key, makes a request
    to the api and returns a json response that gets parsed to a python dictionary
    """

    data_type = 'json'
    endpoint = f"https://api.distancematrix.ai/maps/api/distancematrix/{data_type}"
    params = {"origins": origin, "destinations": destiny, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    api_response = requests.get(url)
    data = api_response.json()

    return data


def get_formated_distance(data):
    
    """
    Takes as a parameter the parsed json data, and loops through it's content, returning the formated
    distance in Kilometers

    """


    distance = ''
    for rows in data['rows']:
        distance = rows['elements'][0]['distance']['text']
    return distance


def get_formated_travel_time(data):
    
    """
    The same as the get_formated_distance function, but this one returns the formated travel time

    """

    duration = ''
    for rows in data['rows']:
        duration = rows['elements'][0]['duration']['text']
    return duration




def get_distance_value(data):
    """
    Function that returns the distance in Kilometers (If you want it to return the distance in meters, just take the /1000 at the end)
    """

    distance = ''
    for rows in data['rows']:
        distance = rows['elements'][0]['distance']['value']
    return distance/1000



def get_time_value(data):

    """
    Function that returns the raw travel_time

    """

    travel_time = ''
    for rows in data['rows']:
        travel_time = rows['elements'][0]['distance']['value']
    return travel_time
