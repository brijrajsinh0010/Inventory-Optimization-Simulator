```python
"""
Application Entry Point
Smart Inventory Optimization System
"""

import argparse
import sys

from src.main import run_application


def main():
    parser = argparse.ArgumentParser(
        description="Smart Inventory Optimization System"
    )

    parser.add_argument(
        "--csv",
        default="data/inventory_sample.csv",
        help="Path to the inventory CSV file.",
    )

    parser.add_argument(
        "--budget",
        type=float,
        default=15000,
        help="Available purchasing budget in rupees.",
    )

    parser.add_argument(
        "--horizon",
        type=int,
        default=7,
        help="Planning horizon in days.",
    )

    parser.add_argument(
        "--search",
        help="Search for a product by ID.",
    )

    args = parser.parse_args()

    if args.budget < 0:
        parser.error("Budget cannot be negative.")

    if args.horizon < 1:
        parser.error("Planning horizon must be at least 1 day.")

    try:
        run_application(
            csv_file=args.csv,
            budget=args.budget,
            planning_horizon=args.horizon,
            search_id=args.search,
        )

    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
