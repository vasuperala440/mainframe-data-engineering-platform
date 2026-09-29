def read_file(file_path):
    with open(file_path, "r") as file:
        all_lines = file.readlines()
        return(all_lines)

def write_file(file_path,record):
    with open(file_path, "a") as file:
        file.write(str(record))       

def parse_customer_record(lines):
    total_records = len(lines)
    Valid_Records = 0
    print("INFO - Pipeline started\n")
    for line in lines:
        fields = line.strip("\n").strip().split("|")

        if len(fields) != 3:
                write_file("data/rejected/customers_rejected.txt",line)
                print("Error : Invalid record")

        else:
            customers = {
                "customer_id": fields[0],
                "customer_name": fields[1],
                "state": fields[2]
            }
            
            if not customers["customer_id"]:
                write_file("data/rejected/customers_rejected.txt",line)
                print("INFO - Invalid record: customer id missing")
        
            if not customers["customer_name"]:
                write_file("data/rejected/customers_rejected.txt",line)
                print("INFO - Invalid record: customer name missing")
        
            if not customers["state"]:
                write_file("data/rejected/customers_rejected.txt",line)
                print("INFO - Invalid record: customer state missing")

            if fields[0] and fields[1] and fields[2] != "":
                print(f"INFO - Valid record: {customers["customer_id"]}")
                Valid_Records = Valid_Records + 1

    print(f"\nINFO - Records processed: {total_records}")
    print(f"INFO - Valid Records: {Valid_Records}")
    print(f"INFO - Invalid Records: {total_records - Valid_Records}")
    return("\nINFO - Pipeline completed")


if __name__ == "__main__":
    line = read_file("data/raw/customers_test.txt")
    pipeline_status = parse_customer_record(line)
    print(pipeline_status)


