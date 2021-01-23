# Stephen Duncanson
# chap.py - Connecticut Historical Aerial Photography

from chap_lib import survey_years
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic

GOOGLE_API_KEY = ''
geolocator = GoogleV3(api_key=GOOGLE_API_KEY)

address_input = input("Enter an address: ")
address = geolocator.geocode(address_input)
address_lat_lon = (address.latitude, address.longitude)

for year in survey_years:
    distance = 999 # arb. distance initalized for brute force
    closest_url = '' #string to hold closest photo url
    for photo_lat_lon, photo_url in survey_years[year].items():
        test_distance = geodesic(address_lat_lon, photo_lat_lon).miles
        if test_distance < distance:
            distance = test_distance
            closest_url = photo_url
    print('{:<4}: Closest photo is {:<6.6} miles away. Link: {:<20}'.format(year, distance, closest_url))
