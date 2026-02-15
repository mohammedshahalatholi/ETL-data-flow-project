import psycopg2

import psycopg2

conn = psycopg2.connect(
    dbname="datareport",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)
cur=conn.cursor()
print("Connected successfully")

cur.execute("select * from etlsolar.solar_wind_data")

data=cur.fetchall()

for i in data:
    print(i)

cur.close()

conn.close()