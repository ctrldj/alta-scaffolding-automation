#!/usr/bin/env python3
"""Loads master_inventory.xlsx, totals each item, and prints low-stock alerts."""

import os
import sys

import pandas as pd

def main():
    inventory_file = "master_inventory.xlsx"
    if not os.path.isfile(inventory_file):
        print(f"Error: '{inventory_file}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        df = pd.read_excel(inventory_file)
    except Exception as e:
        print(f"Error reading '{inventory_file}': {e}", file=sys.stderr)
        sys.exit(1)

    # Expect columns: ItemName, Qty, ReorderPoint
    grouped = df.groupby("ItemName").agg({"Qty": "sum", "ReorderPoint": "first"})

    for item, row in grouped.iterrows():
        qty = row["Qty"]
        reorder = row["ReorderPoint"]
        print(f"{item}: Total Qty = {qty}")
        if qty < reorder:
            print(f"ALERT: '{item}' is below reorder point ({qty} < {reorder})")

if __name__ == "__main__":
    main()