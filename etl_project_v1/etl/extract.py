from utils import logger_support,postger_support
from utils import common_utils
def extract_data():
    logger=logger_support.setip_logger("extract_data")
    try:
        conn=postger_support.connect_to_db()
        logger.info("database connection established successfully")
        data=common_utils.get_data(conn)
        
        logger.info("data extracted successfully",data)
        logger.info("data extracted successfully")
        return data
    except Exception as e:
        logger.error("error connecting to database: %s",e)
        return None