import sys
import pandas as pd
import pyspark


def main():
    print("Data Engineering Environment")
    print("----------------------------")
    print(f"Python: {sys.version}")
    print(f"Pandas: {pd.__version__}")
    print(f"PySpark: {pyspark.__version__}")


if __name__ == "__main__":
    main()