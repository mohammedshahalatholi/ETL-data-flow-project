from etl import extract,transform,load
from utils import logger_support
logger_support.setip_logger("main").info("ETL process started")
def main():
    data=extract.extract_data()
    if data is not None:
        print("data extracted successfully",data)
        transformed_data=transform.transform_data(data)
        if transformed_data is not None:
            logger_support.setip_logger("main").info("data transformed successfully%s",transformed_data)   
            print("data transformed successfully")
            if transformed_data is not None:
                load.load_data(transformed_data)
            
            

        else:
            print("data transformation failed")

    
    







if __name__=="__main__":
    main()