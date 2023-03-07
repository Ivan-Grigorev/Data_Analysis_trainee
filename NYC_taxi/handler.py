from geopy.geocoders import Nominatim
import pandas as pd


def get_rides_of_the_day(data, start_date: None, start_time: str, end_date: None, end_time: str):
    try:
        # Convert pickup_datetime column to datetime dtype
        data["pickup_datetime"] = pd.to_datetime(data["pickup_datetime"], format="%Y-%m-%d %H:%M:%S")

        # Filter DataFrame by date and time range
        result = data.loc[
            (data["pickup_datetime"].dt.date >= pd.to_datetime(start_date).date()) &
            (data["pickup_datetime"].dt.date <= pd.to_datetime(end_date).date()) &
            (data["pickup_datetime"].dt.time >= pd.to_datetime(start_time).time()) &
            (data["pickup_datetime"].dt.time <= pd.to_datetime(end_time).time())
        ]

        return result.sort_values(by="pickup_datetime", ascending=True)

    except AttributeError as err:
        # Display error message in error case
        print(f"WARNING! Function {get_rides_of_the_day.__name__}() in module handler.py gives an error - {err}!")


def get_addresses(pickup_coordinates: [tuple], dropoff_coordinates: [tuple]):
    # Returns the address for a given latitude and longitude using geopy
    geolocator = Nominatim(user_agent="NYC_taxi")

    pickup_location = [geolocator.reverse(f"{str(_[0])}, {str(_[1])}").address for _ in pickup_coordinates]
    dropoff_location = [geolocator.reverse(f"{str(_[0])}, {str(_[1])}").address for _ in dropoff_coordinates]

    return pickup_location, dropoff_location


"""
pickup_coordinates = [
    (40.77887344360352, -73.95391845703125),
    (40.73174285888672, -73.98831176757811),
]

dropoff_coordinates = [
    (40.77116394042969, -73.96387481689453),
    (40.69493103027344, -73.9947509765625),
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
