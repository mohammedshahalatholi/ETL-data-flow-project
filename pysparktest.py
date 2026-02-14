from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BasicPySpark") \
    .getOrCreate()
data = [
    (1, "Alice", 3000),
    (2, "Bob", 4000)
]

df = spark.createDataFrame(data, ["id", "name", "salary"])
df.show()
