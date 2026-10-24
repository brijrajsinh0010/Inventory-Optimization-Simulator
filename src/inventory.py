```python
"""
Inventory Data Management
Project: Smart Inventory Optimization System

Responsibilities:
    - Represent inventory products.
    - Validate product data.
    - Load inventory records from CSV files.
"""

import csv
from dataclasses import dataclass


@dataclass
class Product:
    """Represents a product in the inventory."""

    product_id: str
    name: str
    stock: int
    reorder_level: int
    daily_demand: float
    unit_cost: float

    def validate(self):
        """Validate the product's attributes."""

        if not self.product_id.strip():
            raise ValueError("Product ID cannot be empty.")

        if not self.name.strip():
            raise ValueError("Product name cannot be empty.")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")

        if self.reorder_level < 0:
            raise ValueError("Reorder level cannot be negative.")

        if self.daily_demand < 0:
            raise ValueError("Daily demand cannot be negative.")

        if self.unit_cost < 0:
            raise ValueError("Unit cost cannot be negative.")


def load_inventory_from_csv(filename):
    """Load and validate inventory records from a CSV file."""

    products = []

    required_columns = {
        "product_id",
        "name",
        "stock",
        "reorder_level",
        "daily_demand",
        "unit_cost",
    }

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("The CSV file is empty or missing its header.")

        missing_columns = required_columns - set(reader.fieldnames)

        if missing_columns:
            raise ValueError(
                "Missing CSV columns: "
                + ", ".join(sorted(missing_columns))
            )

        for row_number, row in enumerate(reader, start=2):
            try:
                product = Product(
                    product_id=row["product_id"].strip(),
                    name=row["name"].strip(),
                    stock=int(row["stock"]),
                    reorder_level=int(row["reorder_level"]),
                    daily_demand=float(row["daily_demand"]),
                    unit_cost=float(row["unit_cost"]),
                )

                product.validate()
                products.append(product)

            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Invalid inventory data on CSV row {row_number}: "
                    f"{error}"
                ) from error

    return products


if __name__ == "__main__":

    try:
        inventory = load_inventory_from_csv(
            "data/inventory_sample.csv"
        )

        print(f"Successfully loaded {len(inventory)} products.")

        for product in inventory:
            print(product)

    except (OSError, ValueError) as error:
        print(f"Error loading inventory: {error}")
```
