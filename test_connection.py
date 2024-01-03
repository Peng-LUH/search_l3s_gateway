import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


host= os.getenv("POSTGRES_HOST")
user=os.getenv("postgres")
password= os.getenv("admin")
database= os.getenv("SearchDB")
port = os.getenv("POSTGRES_PORT")


def is_database_connected():
    try:
        connection = psycopg2.connect(
            host= host,
            user= user,
            password= password,
            database=database,
            port = port
        )
        connection.close()
        return True
    except Exception as e:
        return False

# Example usage
if is_database_connected():
    print("Database is connected")
else:
    print("Database connection failed")


