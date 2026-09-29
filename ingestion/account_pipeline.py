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

        if len(fields) != 4:
                write_file("data/rejected/accounts_rejected.txt",line)
                print("Error : Invalid record")

        else:
            customers = {
                "account_id": fields[0],
                "customer_id": fields[1],
                "account_type": fields[2],
                "status": fields[3]
            }
            
            if not customers["account_id"]:
                write_file("data/rejected/accounts_rejected.txt",line)
                print("INFO - Invalid record: account_id id missing")

            if not customers["customer_id"]:
                            write_file("data/rejected/accounts_rejected.txt",line)
                            print("INFO - Invalid record: customer_id id missing")

            if not customers["account_type"]:
                write_file("data/rejected/accounts_rejected.txt",line)
                print("INFO - Invalid record: customer name missing")
        
            if not customers["status"]:
                write_file("data/rejected/accounts_rejected.txt",line)
                print("INFO - Invalid record: customer state missing")

            if fields[0] and fields[1] and fields[2] and fields[3] != "":
                print(f"INFO - Valid record: {customers["account_id"]}")
                Valid_Records = Valid_Records + 1

    print(f"\nINFO - Records processed: {total_records}")
    print(f"INFO - Valid Records: {Valid_Records}")
    print(f"INFO - Invalid Records: {total_records - Valid_Records}")
    return("\nINFO - Pipeline completed")


if __name__ == "__main__":
    line = read_file("data/raw/cust_accounts_test.txt")
    pipeline_status = parse_customer_record(line)
    print(pipeline_status)


