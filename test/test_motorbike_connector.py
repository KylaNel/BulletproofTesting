import unittest
from unittest.mock import patch, call
from src.Motorbike.MotorBikeConnector import MotorBikeConnector


class TestMotorBikeConnector(unittest.TestCase):

    @patch('src.Motorbike.Internet.frequests.post')
    @patch('builtins.print')
    def test_check_if_bike_exists_returns_404(self, mock_print, mock_post):
        # This one is done for you :)
        # Arrange
        mock_post.return_value.status_code = 404
        mock_post.return_value.text = "Page not found"

        # Act
        connector = MotorBikeConnector()
        result = connector.check_if_bike_exists("Harley Davidson")

        # Assert mock called
        mock_post.assert_called_with(url="www.bikernet.com/checkExist", json={'bikeName': "Harley Davidson"})

        # Assert mock returned right calls using assertEqual or else
        # TODO
        # Assert that mock_print was called with the right strings (if you are stuck look at the readme on how to use assert_has_calls
        # TODO
        return

    @patch('src.Motorbike.Internet.frequests.post')
    def test_check_if_bike_exists(self, mock_post):
        #Check if mock_post returns 200 status code and "True" as text, check_if_bike_exist returns "True" as a result
        #Also check/assert that your mock was called with the parameter's you expect (correct url and correct json payload)
        # Arrange

        # Act

        # Assert

        # Assert
        return


    def test_check_if_bike_exists_with_exception(self):
        #Here the post request should return with an exception
        #Then call checkIfBikeExists and check that the return value is None and that mocked print was called with the right params
        #Try and find a different method than assert_has_calls as you are only calling print once
        # Arrange

        # Act


        # Assert

        return

    def test_get_price_for_bike(self):
        # Arrange


        # Act


        # Assert

        # Assert

        return

    def test_get_price_for_bike_gives_404(self):
        # Arrange


        # Act


        # Assert

        return

    def test_get_price_for_bike_raises_exception(self):
        # Arrange


        # Act


        # Assert

        return



if __name__ == '__main__':
    unittest.main()
