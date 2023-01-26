import sys
import sqlite3

from src.CarResolver import CarResolver
from src.CarApiClient import CarApiClient
from src.CarRepository import CarRepository
from src.Motorbike.MotorBikeConnector import MotorBikeConnector

"""
To run the application, type:

    python3 main.py ManufacturerName
    
on the command line and hit enter.

Available manufacturers: Ford, BMW, Honda, Tesla.
"""


def main(car_resolver):
    if len(sys.argv) < 2:
        exit('Add an argument')

    cars = car_resolver.get_all_cars(sys.argv[1])

    if len(cars) > 0:
        for car in cars:
            print(car[1], car[2])
    #motorbike_connector = MotorBikeConnector()
    #print(motorbike_connector.check_if_bike_exists("Honda"))
    #print(motorbike_connector.get_price_for_bike("Honda"))




def initialise_db():
    conn = sqlite3.connect('car_database')
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


"""
Initialize everything...
P.S. Never commit your API keys to your codebase! These should be added using environment variables on the server.
"""
if __name__ == "__main__":
    db_connection = initialise_db()

    main(
        car_resolver=CarResolver(
            car_api_client=CarApiClient(
                api_key='adsf2354adf4Xadf',
            ),
            car_repository=CarRepository(
                db_connection=db_connection,
            ),
        ),
    )
