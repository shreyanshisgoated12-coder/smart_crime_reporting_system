import spacy
from geopy.geocoders import Nominatim
import requests
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="crime_app")
spc = spacy.load("en_core_web_sm")


def extract_loc(text):
    doc = spc(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC", "FAC"]]

    if not locations:
        print("Could not detect location automatically")
        manual = input("Please enter your location: ")
        locations = [manual]

    return locations


def get_coord(text):
    locations = extract_loc(text)
    if not locations:
        return None

    location_query = " ".join(locations)
    location = geolocator.geocode(location_query)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

geolocator = Nominatim(user_agent="crime_app")

def nearest_police_station(coords):
    lat, lon = coords
    
    try:
        # Search for police stations near the location
        location = geolocator.reverse(f"{lat}, {lon}", language="en")
        city = location.raw['address'].get('city') or location.raw['address'].get('town')
        
        # Search police station in that city
        station = geolocator.geocode(f"police station {city} India")
        
        if station:
            dist = geodesic(coords, (station.latitude, station.longitude)).km
            return {
                "name": station.address,
                "distance": round(dist, 2),
                "coords": (station.latitude, station.longitude)
            }
        else:
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None


coords = (28.6315, 77.2167)
station = nearest_police_station(coords)
print(station)
