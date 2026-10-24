# Inventory-Optimization-Simulator
# Smart Inventory Optimization System

An algorithm-driven inventory management project that demonstrates sorting, searching, and greedy replenishment planning to support inventory analysis and purchasing decisions.

## Overview

The Smart Inventory Optimization System is a Python-based project developed to explore the practical application of Data Structures and Algorithms (DSA) in inventory management.

The system processes product inventory data, identifies products requiring replenishment, calculates suggested order quantities, and prepares a replenishment plan subject to a specified budget.

It also includes an algorithm benchmarking module and automated tests.

## Key Features

- **Inventory Management:** Load and process product data from CSV files.
- **Merge Sort:** Sort inventory records by product attributes.
- **Binary Search:** Search sorted inventory records using product IDs.
- **Replenishment Calculations:** Estimate replenishment quantities using stock levels and daily demand.
- **Greedy Budget Allocation:** Prioritize replenishment candidates while respecting the available budget.
- **Algorithm Benchmarking:** Measure execution times for different input sizes.
- **Automated Testing:** Verify core algorithm functionality with Python's `unittest` framework.
- **CSV Reporting:** Save benchmark results for further analysis.

## Project Structure

```text
Smart-Inventory-Optimization-System/
├── algorithms/
│   ├── __init__.py
│   ├── merge_sort.py
│   ├── binary_search.py
│   ├── greedy_replenishment.py
│   └── reorder_logic.py
├── benchmarking/
│   ├── __init__.py
│   └── benchmark_algorithms.py
├── data/
│   └── inventory_sample.csv
├── results/
│   └── benchmark_results.csv
├── src/
│   ├── __init__.py
│   ├── inventory.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_merge_sort.py
│   ├── test_binary_search.py
│   └── test_reorder_logic.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

*The benchmark results file is generated after running the benchmark script.*

## Technologies Used

- Python 3
- CSV data processing
- Data Structures and Algorithms
- Python `unittest`
- Command-line interface
- Git and GitHub

## Algorithms and Complexity

| Algorithm | Purpose | Time Complexity | Auxiliary Space |
|---|---|---|---|
| Merge Sort | Sort inventory records | O(n log n) | O(n) |
| Binary Search | Find a product in sorted records | O(log n) | O(1) for the iterative implementation |
| Greedy Replenishment | Select affordable replenishment orders | O(n log n) for sorting, followed by O(n) selection | O(n) for the resulting plan |

**Note:** The Binary Search complexity assumes an iterative implementation. Merge Sort and greedy-plan complexity refer to the current implementations and exclude unrelated file I/O.

## Installation

### 1. Install Python

Install Python 3 from the official Python website and ensure it is available from your terminal.

### 2. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 3. Enter the project directory

```bash
cd Smart-Inventory-Optimization-System
```

### 4. Run the application

```bash
python run.py
```

### 5. Search for a product

```bash
python run.py --search P106
```

### 6. Change the purchasing budget

```bash
python run.py --budget 20000
```

### 7. Change the planning horizon

```bash
python run.py --horizon 15
```

### 8. Combine command-line options

```bash
python run.py --budget 20000 --horizon 15 --search P106
```

## Run Algorithm Benchmarks

From the project root, execute:

```bash
python -m benchmarking.benchmark_algorithms
```

The benchmark script measures execution times for Merge Sort and Binary Search and saves its results to:

```text
results/benchmark_results.csv
```

Execution times depend on the hardware and software environment.

## Run Automated Tests

Execute the test suite with:

```bash
python -m unittest discover -s tests -v
```

The tests cover sorting, searching, and replenishment calculations.

## Input Data Format

The inventory CSV file uses the following columns:

| Column | Description |
|---|---|
| `product_id` | Unique product identifier |
| `name` | Product name |
| `stock` | Current available stock |
| `reorder_level` | Stock threshold for replenishment |
| `daily_demand` | Estimated daily product demand |
| `unit_cost` | Cost per unit |

Sample data is available in `data/inventory_sample.csv`.

## Sample Use Case

Consider a product whose available stock is below its reorder level. The system can calculate a suggested replenishment quantity using the configured planning horizon and daily demand.

The replenishment planner then considers the candidate orders in priority order and selects those that fit within the available budget.

The output is intended as an educational demonstration of algorithmic inventory planning rather than a production purchasing recommendation.

## Limitations

- The sample inventory is stored in a local CSV file.
- The system uses supplied demand estimates rather than forecasting future demand.
- The greedy replenishment strategy is a heuristic and does not guarantee a globally optimal purchasing plan.
- Results depend on the quality of the supplied inventory data.
- Benchmark measurements vary across machines and execution environments.

## Future Improvements

- Add an interactive inventory dashboard.
- Visualize benchmark results using charts.
- Add database integration.
- Implement demand forecasting.
- Compare greedy planning with dynamic programming.
- Add inventory alerts and low-stock notifications.
- Expand test coverage for invalid input and budget edge cases.

## Academic Purpose

This project demonstrates the application of Data Structures and Algorithms to a practical inventory management problem. It is suitable for academic exploration, algorithm analysis, and further software development.

## License

This project is available for educational use. Add a specific open-source license before distributing it under formal licensing terms.
