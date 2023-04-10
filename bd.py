import psycopg2
from psycopg2 import Error

try:
    # Connetcting to database
    connection = psycopg2.connect(user='postgres', password='12345', host='localhost', database='phones')
        
    cursor = connection.cursor()
    print('Info about PostgreSQL')
    print(connection.get_dsn_parameters(), "\n")
   
    cursor.execute("SELECT version();")
    
    record = cursor.fetchone()
    print("You are now connected to - ", record, "\n")

    cursor.execute("SELECT * FROM sotrudniki")
    sotrudniki = cursor.fetchall()
    print(sotrudniki)


except (Exception, Error) as error:
    print("Error with PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed")