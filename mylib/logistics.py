"""
This module deals with logistics and calculates distances between two points.
Also, it calculates the time taken to travel between two points given a speed.
"""

from geopy import distance

# build a list of cities and their coordinates
cities = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Philadelphia": (39.9526, -75.1652),
    "San Antonio": (29.4241, -98.4936),
    "San Diego": (32.7157, -117.1611),
    "Dallas": (32.7767, -96.7970),
    "San Jose": (37.3382, -121.8863),
    "Austin": (30.2672, -97.7431),
    "Jacksonville": (30.3322, -81.6557),
    "Fort Worth": (32.7555, -97.3308),
    "Columbus": (39.9612, -82.9988),
    "Charlotte": (35.2271, -80.8431),
}


# get the distance between two cities in kilometers
def get_distance(city1, city2):
    """
    This function takes two city names as input and returns the distance between them in kilometers.
    """
    if city1 not in cities or city2 not in cities:
        raise ValueError("One or both cities are not in the list.")

    coords_1 = cities[city1]
    coords_2 = cities[city2]

    distance_km = distance.distance(coords_1, coords_2).km
    return distance_km


# calculate the total distance between a dictionary of cities
def total_distance(city_dict):
    """
    This function takes a dictionary of city names as input and returns the total distance between them in kilometers.
    """
    total_distance_km = 0
    for i in range(len(city_dict) - 1):
        city1 = list(city_dict.keys())[i]
        city2 = list(city_dict.keys())[i + 1]
        total_distance_km += get_distance(city1, city2)

    return total_distance_km


# estimates the travel time between two cities given a speed in km/h
def estimate_travel_time(city1, city2, speed_kmh=80):
    """
    This function takes two city names and a speed in km/h as input and returns the estimated travel time in hours.
    """
    dist = get_distance(city1, city2)
    travel_time_hours = dist / speed_kmh
    return travel_time_hours
