from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.createDataFrame([dict(c = 1, d = 2)])

if __name__ == '__main__':
    df.show()