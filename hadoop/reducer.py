import sys
from collections import defaultdict

# Reducer to sum up quantities for each drug
drug_sales = defaultdict(int)

for line in sys.stdin:
    drug, quantity = line.strip().split("\t")
    drug_sales[drug] += int(quantity)

for drug, total in drug_sales.items():
    print(f"{drug}\t{total}")  # Emit: DrugName\tTotalQuantity

