import time

from src.Exception.ManufacturerNotFoundException import ManufacturerNotFoundException

"""
This class mimics the behaviour of an API client.
In the real world, you would be calling an external API client and receiving a response,
but for the purposes of this workshop, it simply returns some values within the method.
"""


class CarApiClient:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def manifacturer_is_not_bankrupt(self, manufacturer):
        # This API is slow...
        time.sleep(5)

        # Good, old, trusted!
        if manufacturer in ['Ford', 'BMW', 'Honda']:
            return True

        # Oh oh...
        if manufacturer == 'Tesla':
            return False

        raise ManufacturerNotFoundException('Manufacturer not found')
