import unittest

from src.CarApiClient import CarApiClient
from src.Exception.ManufacturerNotFoundException import ManufacturerNotFoundException

"""
This is the test class for CarApiClient.

In the setUp method we initialise the original class. It has no dependencies, so no mocks are used.

We have added a 'happy' test case scenario - 'test_manufacturer_is_not_bankrupt',
as well as a 'failure' test case scenario - 'test_unknown_manufacturer_raises_exception'.

Now ook at the original CarApiClient class.

Can you identify any 'failure' cases that you still need to cover?

Try to write the missing test case. Make sure you think of a good name for it!
"""


class CarApiClientTest(unittest.TestCase):
    def setUp(self):
        # Initialise the API client
        self.car_api_client = CarApiClient(self)

    def test_manufacturer_is_not_bankrupt(self):
        # Arrange
        expected = True

        # Act
        connected = self.car_api_client.manifacturer_is_not_bankrupt('Ford')

        # Assert
        self.assertEqual(expected, connected)

    def test_unknown_manufacturer_raises_exception(self):
        with self.assertRaises(ManufacturerNotFoundException):
            self.car_api_client.manifacturer_is_not_bankrupt('Unknown')


if __name__ == '__main__':
    unittest.main()
