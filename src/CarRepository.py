# exclude from mutation testing

"""
This class is a repository class that has a connection to the database.
It holds methods for retrieving cars from the cars table.
"""


class CarRepository:

    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def find_all_cars(self, manufacturer):
        cursor = self.db_connection.cursor()

        cursor.execute("SELECT * FROM cars WHERE brand=?", (manufacturer,))

        return cursor.fetchall()
