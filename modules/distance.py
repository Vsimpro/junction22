from geopy.geocoders import Nominatim
from geopy import distance


def calculate_distance(Input_place1, Input_place2):
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Get location of the input strings
    place1 = geolocator.geocode(Input_place1)
    place2 = geolocator.geocode(Input_place2)


    # Get latitude and longitude
    Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
    Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

    location1 = (Loc1_lat, Loc1_lon)
    location2 = (Loc2_lat, Loc2_lon)

    return distance.distance(location1, location2).km

"""
Input_place1 = "Mannerheimintie 3"
Input_place2 = "Merimiehenkatu 32"

print(calculate_distance(Input_place1, Input_place2))
"""