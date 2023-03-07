import unittest
from NYC_taxi.orders_addresses import get_addresses


class TestGetAddress(unittest.TestCase):
    def test_attributes(self):
        # Test that all attributes correct
        pickup_coordinates = [('40.77887344360352', '-73.95391845703125')]
        dropoff_coordinates = [('40.77116394042969', '-73.96387481689453')]
        pickup_address, dropoff_address = get_addresses(pickup_coordinates, dropoff_coordinates)

        self.assertEqual(len(pickup_coordinates), len(dropoff_coordinates))
        self.assertTrue(type(pickup_coordinates) is list)
        self.assertTrue(type(dropoff_coordinates) is list)

        self.assertIsNotNone(pickup_address)
        self.assertIsNotNone(dropoff_address)

    def test_result(self):
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
