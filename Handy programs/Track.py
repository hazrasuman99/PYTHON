from geopy.geocoders import Nominatim
import time
from pprint import pprint

# instantiate a new Nominatim client
app = Nominatim(user_agent="tutorial")

# get location raw data
location = app.geocode("Nairobi, Kenya").raw
# print raw data
# pprint(location)

def get_location_by_address(address):
    """This function returns a location as raw from an address
    will repeat until success"""
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)

address = "Main Road Kanchili, Srikaulam, India"
location = get_location_by_address(address)
latitude = location["lat"]
longitude = location["lon"]
# print(f"{latitude}, {longitude}")
# # print all returned data
# pprint(location)

def get_address_by_location(latitude, longitude, language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)