import csv
import mysql.connector


class CitiesSQL:

    @staticmethod
    def cities_main():
        with mysql.connector.connect(user="sql7603182", password="ZIjSBRUVsh", host="sql7.freemysqlhosting.net",
                                     database="sql7603182") as connection:
            cursor = connection.cursor()

            with open("cities.csv") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row['2021'] and row['2021'] != '-':
                        previous_position = int(row['2021'])
                    else:
                        previous_position = 0

                    sql = f"""INSERT INTO 
                        city(name, country, position, previous_position)
                        VALUES('{row['City']}','{row['Country']}', {int(row['2022'])}, {previous_position})
                    """

                    cursor.execute(sql)

                connection.commit()
