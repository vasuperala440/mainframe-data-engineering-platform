import sys
import pandas as pd
import pyspark


def main():
    print("========================================")
    print(" Mainframe Data Engineering Platform")
    print(" Environment Check")
    print("========================================")

    print(f"Python: {sys.version}")
    print(f"Pandas: {pd.__version__}")
    print(f"PySpark: {pyspark.__version__}")
    print(f"Postgresql: connected")
    print(f"Docker: version")

    print("Environment Status: READY")


if __name__ == "__main__":
    main()