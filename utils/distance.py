from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="carbon-footprint-app")

def calculate_distance(origin_zip: str, destination_zip: str) -> float:
    origin = geolocator.geocode(origin_zip)
    destination = geolocator.geocode(destination_zip)

    if not origin or not destination:
        raise Exception("Invalid ZIP / PIN code")

    distance_km = geodesic(
        (origin.latitude, origin.longitude),
        (destination.latitude, destination.longitude)
    ).km

    return round(distance_km, 2)

