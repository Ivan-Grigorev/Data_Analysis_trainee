import pandas as pd

from orders_addresses import get_addresses


pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 1000)


class NYCTaxiAnalysis:

    def __init__(self, dataset):
        self.data = pd.read_csv(dataset).head(30)
        self.pickup_coordinates = None
        self.dropoff_coordinates = None
        self.pickup_address = None
        self.dropoff_address = None

    def pickup_dropoff_addresses(self):
        # This function get all pickup and dropoff addresses by longitude/latitude and add it to dataframe
        self.pickup_coordinates = list(zip(self.data["pickup_latitude"].values,
                                           self.data["pickup_longitude"].values,))
        self.dropoff_coordinates = list(zip(self.data["dropoff_latitude"].values,
                                            self.data["dropoff_longitude"].values,))

        self.pickup_address, self.dropoff_address = get_addresses(self.pickup_coordinates, self.dropoff_coordinates)

        self.data["pickup_address"] = self.pickup_address
        self.data["dropoff_address"] = self.dropoff_address

        return self.data


if __name__ == '__main__':
    nyc_taxi_analysis = NYCTaxiAnalysis("CSV/nyc_taxi_trip_duration.csv")
    print(nyc_taxi_analysis.pickup_dropoff_addresses())
