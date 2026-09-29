from pyspark.sql import SparkSession
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def main():
    spark = (
        SparkSession.builder
        .appName("MainframeDataEngineering")
        .master("local[*]")
        .getOrCreate()
    )

    data = [
        (1, "John", 1000.50),
        (2, "Mary", 2500.75),
        (3, "David", 750.25),
    ]

    columns = ["customer_id", "customer_name", "balance"]

    df = spark.createDataFrame(data, columns)

    df.show()

    spark.stop()


if __name__ == "__main__":
    main()