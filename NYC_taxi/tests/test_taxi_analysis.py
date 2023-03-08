import unittest
import pandas as pd

from NYC_taxi.handler import get_addresses, get_rides_of_the_day


class TestGetRidesOfTheDay(unittest.TestCase):
    def setUp(self):
        # Define sample data for testing
        data = {
            "pickup_datetime": pd.date_range(
                start="2016-01-01 00:00:00", end="2016-01-31 23:59:59", freq="s"
            )
        }
        self.df = pd.DataFrame(data)

    def test_get_rides_of_the_day(self):
        # Define expected output
        start_datetime = pd.to_datetime("2016-01-01 06:00:00")
        end_datetime = pd.to_datetime("2016-01-30 12:00:00")

        # Filter dataframe
        filtered_df = get_rides_of_the_day(
            self.df,
            start_date="2016-01-01",
            start_time="06:00:00",
            end_date="2016-01-30",
            end_time="12:00:00",
        )

        # Check that all values in pickup_datetime are within the expected range
        self.assertTrue(filtered_df["pickup_datetime"].min() >= start_datetime)
        self.assertTrue(filtered_df["pickup_datetime"].max() <= end_datetime)

    def test_get_rides_of_the_day_invalid_input(self):
        # Check if function raises ValueError when inputs are invalid
        with self.assertRaises(ValueError):
            get_rides_of_the_day(
                self.df, "2016-01-01", "2016-01-30", "12:00:00", "06:00:00"
            )
            get_rides_of_the_day(
                self.df, "2016-01-01", "2016-01-01", "06:00:00", "12:00:00"
            )
            get_rides_of_the_day(
                self.df, "2016-01-30", "2016-01-01", "06:00:00", "12:00:00"
            )
            get_rides_of_the_day(
                self.df, "2016-01-01", "2016-01-30", "00:00:00", "24:00:00"
            )


class TestGetAddress(unittest.TestCase):
    def test_get_addresses_attributes(self):
        # Test that all attributes are correct
        pickup_coordinates = [("40.77887344360352", "-73.95391845703125")]
        dropoff_coordinates = [("40.77116394042969", "-73.96387481689453")]
        pickup_address, dropoff_address = get_addresses(
            pickup_coordinates, dropoff_coordinates
        )

        self.assertEqual(len(pickup_coordinates), len(dropoff_coordinates))
        self.assertTrue(type(pickup_coordinates) is list)
        self.assertTrue(type(dropoff_coordinates) is list)

        self.assertIsNotNone(pickup_address)
        self.assertIsNotNone(dropoff_address)

    def test_get_addresses(self):
        # Test that the returned address matches the expected address
        pickup_address, dropoff_address = get_addresses(
            [("40.77887344360352", "-73.95391845703125")],
            [("40.77116394042969", "-73.96387481689453")],
        )
        pickup_expected_address = [
            "1530, 3rd Avenue, Manhattan Community Board 8, "
            "Manhattan, New York County, City of New York, New York, 10028, United States"
        ]
        dropoff_expected_address = [
            "760, Park Avenue, Manhattan Community Board 8, "
            "Manhattan, New York County, City of New York, New York, 11206, United States"
        ]

        self.assertEqual(pickup_address, pickup_expected_address)
        self.assertEqual(dropoff_address, dropoff_expected_address)


if __name__ == "__main__":
    unittest.main()
