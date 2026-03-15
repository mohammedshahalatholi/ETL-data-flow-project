from utils import logger_support


def get_data(conn):
    query="select * from etlsolar.solar_wind_data"
    logger_support.setip_logger("get_data").info("Executing query: %s", query)
    cur=conn.cursor()
    cur.execute(query)
    data=cur.fetchall()
    cur.close()
    return data
