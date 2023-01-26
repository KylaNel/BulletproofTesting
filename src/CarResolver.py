from src.Exception.BankruptManufacturerException import BankruptManufacturerException

"""
This class uses the API client and the repository to return the cars from a specific manufacturer,
firstly checking whether the manufacturer has not gone bankrupt.
"""


class CarResolver:

    def __init__(self, car_repository, car_api_client) -> None:
        self.car_api_client = car_api_client
        self.car_repository = car_repository

    def get_all_cars(self, manufacturer):
        if self.car_api_client.manifacturer_is_not_bankrupt(manufacturer):
            return self.car_repository.find_all_cars(manufacturer)
        else:
            raise BankruptManufacturerException('Manufacturer has gone bankrupt!')
