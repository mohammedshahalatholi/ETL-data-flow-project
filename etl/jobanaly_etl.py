import pandas as pd

from comonfunc import get_data,get_connection



data=get_data()
colums=data.columns
#df=pd.DataFrame(colums,columns=["columns"])

load =data.groupby(["company","year"])["layoffs"].sum()

df=load.reset_index()

conn=get_connection()
try:
    df.to_sql(name="jobanalysis",con=conn,schema="etlsolar",if_exists="replace",index=False)
except Exception as e:
    print("error",e)
    