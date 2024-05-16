# dar-spark-course
### Описание
...
---
# Установка
Создание виртуального окружения:
```bash
python -m venv venv_spark
./venv_spark/Scripts/activate
pip install -Ur requirements.txt
```

Переменные окружения:

- **PYSPARK_PYTHON** = .\spark-3.5.1-bin-hadoop3 
- **SPARK_HOME** = .\spark-3.5.1-bin-hadoop3
- **HADOOP_HOME** = .\venv_spark\Scripts\python.exe

Установка Spark 3.5.1:

[Ссылка](https://spark.apache.org/downloads.html)

# Проверка
Запустить `launch_for_test.py`
```bash
./venv_spark/Scripts/activate
python ./launch_for_test.py
```