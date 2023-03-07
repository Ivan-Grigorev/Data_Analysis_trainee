import unittest
import pandas as pd

from NYC_taxi.handler import get_addresses, get_rides_of_the_day


class TestGetRidesOfTheDay(unittest.TestCase):
    def setUp(self):
        # Create sample data
        data = {'pickup_datetime': ['2016-01-01 00:00:00', '2016-01-05 09:44:31', '2016-01-06 12:30:00',
                                    '2016-01-13 20:25:29', '2016-01-17 19:40:26', '2016-01-21 08:28:19',
                                    '2016-01-22 17:47:13', '2016-01-31 11:59:59'],}
        self.df = pd.DataFrame(data)
        self.df['pickup_datetime'] = pd.to_datetime(self.df['pickup_datetime'])

    def test_get_rides_of_the_day(self):
        # Define expected output
        expected_output = pd.to_datetime(['2016-01-05 09:44:31', '2016-01-13 20:25:29',
                                          '2016-01-17 19:40:26', '2016-01-21 08:28:19',
                                          '2016-01-22 17:47:13'])
        # Filter dataframe
        filtered_df = get_rides_of_the_day(self.df, '2016-01-01', '2016-01-30', '06:00:00', '12:00:00')
        self.assertTrue(filtered_df['pickup_datetime'].equals(expected_output))

        filtered_df = get_rides_of_the_day(self.df, '2016-01-01', '2016-01-04', '06:00:00', '12:00:00')
        self.assertTrue(filtered_df.empty)

    def test_get_rides_of_the_day_invalid_input(self):
        # Check if function raises ValueError when inputs are invalid
        with self.assertRaises(ValueError):
            get_rides_of_the_day(self.df, '2016-01-01', '2016-01-30', '12:00:00', '06:00:00')
            get_rides_of_the_day(self.df, '2016-01-01', '2016-01-01', '06:00:00', '12:00:00')
            get_rides_of_the_day(self.df, '2016-01-30', '2016-01-01', '06:00:00', '12:00:00')
            get_rides_of_the_day(self.df, '2016-01-01', '2016-01-30', '00:00:00', '24:00:00')


class TestGetAddress(unittest.TestCase):
    def test_get_addresses_attributes(self):
        # Test that all attributes are correct
        pickup_coordinates = [('40.77887344360352', '-73.95391845703125')]
        dropoff_coordinates = [('40.77116394042969', '-73.96387481689453')]
        pickup_address, dropoff_address = get_addresses(pickup_coordinates, dropoff_coordinates)

        self.assertEqual(len(pickup_coordinates), len(dropoff_coordinates))
        self.assertTrue(type(pickup_coordinates) is list)
        self.assertTrue(type(dropoff_coordinates) is list)

        self.assertIsNotNone(pickup_address)
        self.assertIsNotNone(dropoff_address)

    def test_get_addresses(self):
        # Test that the returned address matches the expected address
        pickup_address, dropoff_address = get_addresses([('40.77887344360352', '-73.95391845703125')],
                                                        [('40.77116394042969', '-73.96387481689453')])
        pickup_expected_address = ['1530, 3rd Avenue, Manhattan Community Board 8, '
                                   'Manhattan, New York County, City of New York, New York, 10028, United States']
        dropoff_expected_address = ['760, Park Avenue, Manhattan Community Board 8, '
                                    'Manhattan, New York County, City of New York, New York, 11206, United States']

        self.assertEqual(pickup_address, pickup_expected_address)
        self.assertEqual(dropoff_address, dropoff_expected_address)


if __name__ == '__main__':
    unittest.main()
