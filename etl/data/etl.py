import psycopg2

conn=psycopg2.connect(
    dbname="datareport",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"

)

cur=conn.cursor()

cur.execute("select * from etlsolar.solar_wind_data")
data=cur.fetchone()
print(data)


cur.execute("""
    CREATE TABLE IF NOT EXISTS etlsolar.loadeddata (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        proton_density_cm3 DECIMAL(10, 2)
    );
""")


