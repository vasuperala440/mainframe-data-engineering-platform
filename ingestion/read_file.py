def read_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())
            fields = line.strip().split("|")
            customers = {
                    "customer_id": fields[0],
                    "customer_name": fields[1],
                    "state": fields[2]
                }


if __name__ == "__main__":
    read_file("data/raw/customers_test.txt")

print(customers)

def parse_customer_record(line):
    fields = line.strip().split("|")

    return {
        "customer_id": fields[0],
        "customer_name": fields[1],
        "state": fields[2]
    }


