
from utils import logger_support
def transform_data(data):
    logger=logger_support.setip_logger("transform_data")
    try:
        transformed_data=[{"id":row[0],"solar_power":row[1],"wind_power":row[2],"timestamp":row[3]} for row in data]
        addcolumtn="total_power"
        for row in transformed_data:
            row[addcolumtn]=row["wind_power"]>360
        logger.info("data transformed successfully",transformed_data)
        
        return transformed_data
    except Exception as e:
        logger.error("error transforming data: %s",e)
        return None