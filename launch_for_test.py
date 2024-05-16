from pyspark.sql.session import SparkSession
spark = SparkSession.builder.getOrCreate()
spark.createDataFrame([dict(c = 1)]).show()