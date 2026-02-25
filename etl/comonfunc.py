import pandas as pd
from sqlalchemy import create_engine
import psycopg2
def get_data():
    datas=pd.read_csv("etl/data/job_laydata/tech_employment_2000_2025.csv")
    return datas

def get_connection():
    engine=create_engine( "postgresql+psycopg2://postgres:admin@localhost:5432/datareport")
    return engine
