from geopy.geocoders import Nominatim


def get_addresses(pickup_coordinates: [tuple], dropoff_coordinates: [tuple]):
    geolocator = Nominatim(user_agent='NYC_taxi')
    pickup_location = [geolocator.reverse(f"{str(_[0])}, {str(_[1])}").address for _ in pickup_coordinates]
    dropoff_location = [geolocator.reverse(f"{str(_[0])}, {str(_[1])}").address for _ in dropoff_coordinates]
    return pickup_location, dropoff_location


"""
pickup_coordinates = [
    (40.77887344360352, -73.95391845703125),
    (40.73174285888672, -73.98831176757811),
    (40.721458435058594, -73.997314453125),
    (40.75971984863281, -73.961669921875),
    (40.70846939086913, -74.01712036132812)
]

dropoff_coordinates = [
    (40.77116394042969, -73.96387481689453),
    (40.69493103027344, -73.9947509765625),
    (40.774917602539055, -73.94802856445312),
    (40.780628204345696, -73.95677947998048),
    (40.740631103515625, -73.9881820678711)
]


response = {'place_id': 25467416,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'node',
            'osm_id': 2724236574,
            'lat': '40.7790721',
            'lon': '-73.9540252',
            'display_name': '1530, '
                            '3rd Avenue, Manhattan Community Board 8,'
                            ' Manhattan, New York County, City of New York, New York, 10028, United States',
            'address': {'house_number': '1530',
                        'road': '3rd Avenue',
                        'neighbourhood': 'Manhattan Community Board 8',
                        'suburb': 'Manhattan', 
                        'county': 'New York County',
                        'city': 'City of New York',
                        'state': 'New York',
                        'ISO3166-2-lvl4': 'US-NY',
                        'postcode': '10028',
                        'country': 'United States',
                        'country_code': 'us'},
            'boundingbox': ['40.7790221', '40.7791221', '-73.9540752', '-73.9539752']
            }
"""
