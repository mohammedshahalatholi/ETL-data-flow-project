import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="datareport",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

# -------- Extract --------
df_raw = pd.read_sql("SELECT * FROM etlsolar.solar_wind_data;", conn)

#  CRITICAL FIX → remove timezone BEFORE any Excel write
df_raw["timestamp_utc"] = df_raw["timestamp_utc"].dt.tz_localize(None)

before_df = df_raw.copy()
df_clean = df_raw.copy()

# cleaning example
df_clean = df_clean[df_clean["proton_density_cm3"] >= 5]
df_clean = df_clean.drop_duplicates()
len_befor=len(before_df)
len_after=len(df_clean)
summary_df = pd.DataFrame({
    "metric": ["row_count_before", "row_count_after"],
    "value": [len_befor, len_after]
})
# -------- Export --------
with pd.ExcelWriter("etl\data\solar_wind_comparison_report.xlsx", engine="openpyxl") as writer:
    summary_df.to_excel(writer, sheet_name="summary_df", index=False)
  

conn.close()

print("Excel created successfully")