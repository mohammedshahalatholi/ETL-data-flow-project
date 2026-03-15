import logging

def setip_logger(name,level=logging.INFO):
    logger=logging.getLogger(name)
    #logger folder
    logger.setLevel(logging.INFO)
    handler=logging.FileHandler(f"etl_project_v1/logs/{name}.log")
    logger.addHandler(handler)
    
    return logger


