def read_file(file_path):
    with open(file_path, "r") as file:
        all_lines = file.readlines()
        return(all_lines)

def write_file(file_path,record):
    with open(file_path, "a") as file:
        file.write(str(record))       

def parse_accounts_record(lines):
    total_records = len(lines)
    valid_records = 0
    print("INFO - Pipeline started\n")
    for line in lines:
        fields = line.strip("\n").strip().split("|")

        if len(fields) != 4:
                write_file("data/rejected/accounts_rejected.txt",line)
                print("Error : Invalid record")

        else:
            accounts = {
                "account_id": fields[0],
                "customer_id": fields[1],
                "account_type": fields[2],
                "status": fields[3]
            }
            
            if (accounts["account_id"] 
                and accounts["customer_id"] 
                and accounts["account_type"]
                and accounts["status"]):
                print(f"INFO - Valid record: {accounts['account_id']}")
                valid_records = valid_records + 1

            else:
                write_file("data/rejected/accounts_rejected.txt",line)
                print("INFO - Invalid record: account_data id missing")

    print(f"\nINFO - Records processed: {total_records}")
    print(f"INFO - Valid Records: {valid_records}")
    print(f"INFO - Invalid Records: {total_records - valid_records}")
    return("\nINFO - Pipeline completed")


if __name__ == "__main__":
    line = read_file("data/raw/cust_accounts_test.txt")
    pipeline_status = parse_accounts_record(line)
    print(pipeline_status)


