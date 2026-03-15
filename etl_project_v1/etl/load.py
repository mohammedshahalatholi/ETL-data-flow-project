from utils import logger_support
from utils import postger_support
from utils import common_utils


def load_data(loaded_data):

    logger = logger_support.setip_logger("load_data")
    conn = None

    try:
        conn = postger_support.connect_to_db()
        logger.info("database connection established successfully")

        cur = conn.cursor()

        if table_exists(cur, "etlsolar.loaded_data"):
            logger.info("existing table dropping")
            cur.execute("drop table etlsolar.loaded_data")
            logger.info("existing table dropped successfully")

        logger.info("creating table")
        cur.execute("""
            create table etlsolar.loaded_data (
                id int,
                wind_power float,
                total_power boolean
            )
        """)

        for row in loaded_data:
            cur.execute(
                """
                insert into etlsolar.loaded_data
                (id, wind_power, total_power)
                values (%s,%s,%s)
                """,
                (row["id"], row["wind_power"], row["total_power"])
            )

        conn.commit()
        logger.info("data loaded successfully")

    except Exception as e:
        logger.error("error loading data: %s", e)

    finally:
        if conn:
            conn.close()
            logger.info("database connection closed successfully")


def table_exists(cur, table_name):

    schema, table = table_name.split(".")

    cur.execute(
        """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_schema=%s AND table_name=%s
        )
        """,
        (schema, table)
    )
    print("table exists check executed successfully")

    return cur.fetchone()[0]