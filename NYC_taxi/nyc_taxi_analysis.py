import pandas as pd

from handler import get_addresses, get_rides_of_the_day


pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 1000)


class NYCTaxiAnalysis:
    def __init__(self, dataset, lines=None, date_from=None, date_to=None):
        self.data = pd.read_csv(dataset).head(lines)

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
        self.morning_rides = get_rides_of_the_day(
            data=self.data,
            start_date=self.date_from,
            start_time="06:00:00",
            end_date=self.date_to,
            end_time="12:00:00",
        )
        self.afternoon_rides = get_rides_of_the_day(
            data=self.data,
            start_date=self.date_from,
            start_time="12:00:00",
            end_date=self.date_to,
            end_time="18:00:00",
        )
        self.evening_rides = get_rides_of_the_day(
            data=self.data,
            start_date=self.date_from,
            start_time="18:00:00",
            end_date=self.date_to,
            end_time="23:59:59",
        )
        self.night_rides = get_rides_of_the_day(
            data=self.data,
            start_date=self.date_from,
            start_time="00:00:00",
            end_date=self.date_to,
            end_time="06:00:00",
        )

        return self.morning_rides, self.afternoon_rides, self.evening_rides, self.night_rides

    def pickup_dropoff_addresses(self):
        # This function get all pickup and dropoff addresses by longitude/latitude and add it to dataframe
        self.pickup_coordinates = list(zip(self.data["pickup_latitude"].values,
                                           self.data["pickup_longitude"].values,))
        self.dropoff_coordinates = list(zip(self.data["dropoff_latitude"].values,
                                            self.data["dropoff_longitude"].values,))

        self.pickup_address, self.dropoff_address = get_addresses(self.pickup_coordinates,
                                                                  self.dropoff_coordinates)

        self.data["pickup_address"] = self.pickup_address
        self.data["dropoff_address"] = self.dropoff_address

        return self.data

    def analysis_visualization(self):
        pass


if __name__ == "__main__":
    nyc_taxi_analysis = NYCTaxiAnalysis(dataset="../CSV/nyc_taxi_trip_duration.csv",
                                        date_from="2016-01-01",
                                        date_to="2016-01-30",)

    # nyc_taxi_analysis.pickup_dropoff_addresses()
    print(nyc_taxi_analysis.rides_of_the_day())
    # print(nyc_taxi_analysis.analysis_visualization())
