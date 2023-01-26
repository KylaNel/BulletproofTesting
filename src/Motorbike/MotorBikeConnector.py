from src.Motorbike.Internet import frequests


class MotorBikeConnector:

    def __init__(self):
        self.exist_url = "www.bikernet.com/checkExist"
        self.price_check_url = "www.bikernet.com/getPriceForBike"
        pass

    def check_if_bike_exists(self, bike_name):
        obj = {'bikeName': bike_name}
        try:
            resp = frequests.post(url=self.exist_url, json=obj)
            if resp.status_code == 200:
                return resp.text
            else:
                print("I got a not OK response")
                raise Exception
        except Exception:
            print("Ooops something went wrong")

    def get_price_for_bike(self, bike_name):
        obj = {'bikeName': bike_name}
        try:
            resp = frequests.post(url=self.price_check_url, json=obj)
            if resp.status_code == 200:
                return resp.text
            else:
                print("I got a not OK response")
                raise Exception
        except Exception:
            print("Ooops something went wrong")


