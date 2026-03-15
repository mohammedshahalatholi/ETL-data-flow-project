import psycopg2


def connect_to_db():
    try:
        conn=psycopg2.connect(
            dbname="datareport",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        print("Connected successfully")
        return conn
    except Exception as e:
        print("Error connecting to database:",e)

    