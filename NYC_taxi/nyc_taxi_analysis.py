import pandas as pd
import numpy as np

from geopy import Nominatim

pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 1000)


class NYCTaxiAnalysis:
    def __init__(self, dataset, date_from: str, date_to: str, lines=None):
        # Filter dataset by date
        self.data = pd.read_csv(dataset).query("@date_from <= pickup_datetime <= @date_to").head(lines)

        self.morning_rides = None
        self.afternoon_rides = None
        self.evening_rides = None
        self.night_rides = None
        self.date_from = date_from
        self.date_to = date_to

        self.pickup_coordinates = None
        self.dropoff_coordinates = None
        self.pickup_address = None
        self.dropoff_address = None

    def rides_of_the_day(self):
        # This function analyze taxi rides based on time of day: morning, afternoon, evening, late night/early morning
        try:
            # Convert pickup_datetime column to datetime dtypes
            self.data["pickup_datetime"] = pd.to_datetime(self.data["pickup_datetime"], format="%Y-%m-%d %H:%M:%S")

            # Calculate the number of rides for each time period
            self.morning_rides = self.data.loc[
                (self.data["pickup_datetime"].dt.time >= pd.to_datetime('06:00:00').time()) &
                (self.data["pickup_datetime"].dt.time <= pd.to_datetime('12:00:00').time())
            ].sort_values(by="pickup_datetime", ascending=True)

            self.afternoon_rides = self.data.loc[
                (self.data["pickup_datetime"].dt.time >= pd.to_datetime('12:00:00').time()) &
                (self.data["pickup_datetime"].dt.time <= pd.to_datetime('18:00:00').time())
            ].sort_values(by="pickup_datetime", ascending=True)

            self.evening_rides = self.data.loc[
                (self.data["pickup_datetime"].dt.time >= pd.to_datetime('18:00:00').time()) &
                (self.data["pickup_datetime"].dt.time <= pd.to_datetime('23:59:59').time())
            ].sort_values(by="pickup_datetime", ascending=True)

            self.night_rides = self.data.loc[
                (self.data["pickup_datetime"].dt.time >= pd.to_datetime('00:00:00').time()) &
                (self.data["pickup_datetime"].dt.time <= pd.to_datetime('06:00:00').time())
            ].sort_values(by="pickup_datetime", ascending=True)

            return f"The total rides from {self.date_from} to {self.date_to}, there were:\n" \
                   f"\t{len(self.morning_rides)} rides from 6:00 a.m. (06:00:00) to 12:00 p.m. (12:00:00);\n" \
                   f"\t{len(self.afternoon_rides)} rides from 12:00 p.m. (12:00:00) to 6:00 p.m. (18:00:00);\n" \
                   f"\t{len(self.evening_rides)} rides from 6:00 p.m. (18:00:00) to 12 a.m. (00:00:00);\n" \
                   f"\t{len(self.night_rides)} rides from 12:00 a.m. (00:00:00) to 6:00 a.m. (06:00:00)"

        except KeyError as err:
            # Display error message in error key
            return f"WARNING! The function {NYCTaxiAnalysis.rides_of_the_day.__name__}() error - {err}"

    def pickup_dropoff_addresses(self):
        # This function get all pickup and dropoff addresses by longitude/latitude and add it to dataframe
        pickup_lat = self.data["pickup_latitude"].values
        pickup_lon = self.data["pickup_longitude"].values
        dropoff_lat = self.data["dropoff_latitude"].values
        dropoff_lon = self.data["dropoff_longitude"].values

        # Stack the latitude/longitude arrays horizontally and transpose to create tuples
        self.pickup_coordinates = np.vstack((pickup_lat, pickup_lon)).T
        self.dropoff_coordinates = np.vstack((dropoff_lat, dropoff_lon)).T

        geolocator = Nominatim(user_agent="NYC_taxi")

        self.pickup_address = [geolocator.reverse(coord).address for coord in self.pickup_coordinates]
        self.dropoff_address = [geolocator.reverse(coord).address for coord in self.dropoff_coordinates]

        self.data["pickup_address"] = self.pickup_address
        self.data["dropoff_address"] = self.dropoff_address

        return self.data

    def analysis_visualization(self):
        return self.data


if __name__ == "__main__":
    nyc_taxi_analysis = NYCTaxiAnalysis(dataset="../CSV/nyc_taxi_trip_duration.csv",
                                        date_from='2016-01-01',
                                        date_to='2016-01-30',
                                        lines=10)

    # print(nyc_taxi_analysis.rides_of_the_day())
    # print(nyc_taxi_analysis.pickup_dropoff_addresses())

    print(nyc_taxi_analysis.analysis_visualization())
