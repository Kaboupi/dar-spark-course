from pyspark.sql.session import SparkSession
# Три формата действий - Transformation, Actions, Lazy evaluation
# Создание Spark сессии
spark = SparkSession.builder.getOrCreate()

# Создание Spark DataFrame (Transformation)
df = spark.sql("select 1 a, 2 b, 3 c")

# Изменение списка колонок (Transformation)
df = df.select("b", "a")

# Фильтрация значений (Transformation)
df = df.where("a = 1")

# Вывести данные на экран (Action)
df.show()