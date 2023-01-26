import unittest
import sqlite3
from unittest.mock import MagicMock

from src.CarRepository import CarRepository
from src.CarResolver import CarResolver

from src.Exception.BankruptManufacturerException import BankruptManufacturerException

"""
This is an additional test class for CarResolver.

This test uses the original CarRepository class instead of replacing it with a mock,
which makes it an integration/smoke test.

This is done to ensure that, for example, if the SQL code in CarRepository is changed,
it still works. If we did not have this test, we may encounter a situation where vital
application functionality is down because of some unaccounted changes in the source code.

Try to fill out the TODOs and ?s to get the test to run.
"""

class CarResolverSmokeTest(unittest.TestCase):
    def setUp(self):
        # Create a mock for the car API client
        self.car_api_client = MagicMock()

        # Create a test database
        test_db_connection = self._initialise_db()

        # Initialise the car repository
        self.car_repository = CarRepository(test_db_connection)

        # Create the car resolver with the mocked API client
        self.car_resolver = CarResolver(self.car_repository, self.car_api_client)

    # This method deletes the test data after the test is run to free up space.
    def tearDown(self):
        conn = sqlite3.connect('test_database')
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS cars")

        conn.commit()

    def test_get_all_cars_success(self):
        # Arrange the CarApiClient 'manifacturer_is_not_bankrupt' method to return True.
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = True

        # Act - get all cars for manufacturer 'Ford
        cars = self.car_repository.find_all_cars('Ford')

        # Assert
        self.assertEqual(
            [(1, 'Ford', 'Fiesta'), (2, 'Ford', 'Mustang'), (3, 'Ford', 'Focus')],
            cars,
        )

    # TODO - can you check if the exception is still thrown?
    def test_get_all_cars_failure(self):
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = False
        
        with self.assertRaises(BankruptManufacturerException):
            self.car_resolver.get_all_cars('Tesla')


    # This method creates some fixtures for the test. Have a look if you like, but it ain't pretty!
    def _initialise_db(self):
        conn = sqlite3.connect('test_database')
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS cars")

        c.execute("CREATE TABLE IF NOT EXISTS cars ([id] INTEGER PRIMARY KEY, [brand] TEXT, [model] TEXT)")

        c.execute("INSERT INTO cars values(1, 'Ford', 'Fiesta')")
        c.execute("INSERT INTO cars values(2, 'Ford', 'Mustang')")
        c.execute("INSERT INTO cars values(3, 'Ford', 'Focus')")
        c.execute("INSERT INTO cars values(4, 'BMW', 'M3')")
        c.execute("INSERT INTO cars values(5, 'BMW', 'X5')")
        c.execute("INSERT INTO cars values(6, 'BMW', 'iX')")
        c.execute("INSERT INTO cars values(7, 'Honda', 'Civic')")
        c.execute("INSERT INTO cars values(8, 'Honda', 'Jazz')")
        c.execute("INSERT INTO cars values(9, 'Honda', 'E')")

        conn.commit()

        return conn


if __name__ == '__main__':
    unittest.main()
