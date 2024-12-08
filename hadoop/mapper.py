import sys

# Mapper to calculate total sales for each drug
for line in sys.stdin:
    data = line.strip().split(",")  # Assuming CSV format with columns: DrugName, Quantity
    if len(data) == 2:  # Ensure two fields exist
        print(f"{data[0]}\t{data[1]}")  # Emit: DrugName\tQuantity
