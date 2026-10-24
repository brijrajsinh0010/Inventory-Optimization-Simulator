"""
Algorithm Benchmarking Module
Project: Smart Inventory Optimization System

Measures the execution time of:
1. Merge Sort
2. Binary Search

Results are saved as a CSV file for analysis.
"""

import csv
import random
import time
from pathlib import Path

from algorithms.merge_sort import merge_sort
from algorithms.binary_search import binary_search


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_ROOT / "results"
OUTPUT_FILE = RESULTS_DIR / "benchmark_results.csv"


def benchmark_merge_sort(numbers, repetitions=5):
    """Measure the average execution time of Merge Sort."""

    total_time = 0.0

    for _ in range(repetitions):
        start_time = time.perf_counter()
        merge_sort(numbers)
        end_time = time.perf_counter()

        total_time += end_time - start_time

    return total_time / repetitions


def benchmark_binary_search(sorted_numbers, target, repetitions=1000):
    """Measure the average execution time of Binary Search."""

    total_time = 0.0

    for _ in range(repetitions):
        start_time = time.perf_counter()
        binary_search(sorted_numbers, target)
        end_time = time.perf_counter()

        total_time += end_time - start_time

    return total_time / repetitions


def run_benchmarks():
    """Run benchmarks for different input sizes and save the results."""

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    input_sizes = [100, 500, 1000, 5000, 10000]
    repetitions = 5

    random_generator = random.Random(42)
    results = []

    print("=" * 65)
    print("SMART INVENTORY OPTIMIZATION SYSTEM")
    print("ALGORITHM PERFORMANCE BENCHMARK")
    print("=" * 65)

    for size in input_sizes:
        numbers = random_generator.sample(range(size * 10), size)

        # Benchmark Merge Sort
        merge_sort_time = benchmark_merge_sort(
            numbers,
            repetitions=repetitions,
        )

        # Prepare sorted data before measuring Binary Search.
        sorted_numbers = sorted(numbers)
        target = sorted_numbers[-1]

        # Benchmark Binary Search
        binary_search_time = benchmark_binary_search(
            sorted_numbers,
            target,
            repetitions=1000,
        )

        results.append({
            "input_size": size,
            "merge_sort_avg_seconds": f"{merge_sort_time:.10f}",
            "binary_search_avg_seconds": f"{binary_search_time:.10f}",
            "merge_sort_repetitions": repetitions,
            "binary_search_repetitions": 1000,
        })

        print(f"\nInput Size: {size:,}")
        print(f"Merge Sort Average: {merge_sort_time:.8f} seconds")
        print(f"Binary Search Average: {binary_search_time:.8f} seconds")

    # Write benchmark results to CSV.
    fieldnames = [
        "input_size",
        "merge_sort_avg_seconds",
        "binary_search_avg_seconds",
        "merge_sort_repetitions",
        "binary_search_repetitions",
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\n" + "=" * 65)
    print("BENCHMARK COMPLETED SUCCESSFULLY")
    print(f"Results saved to: {OUTPUT_FILE}")
    print("=" * 65)


if __name__ == "__main__":
    run_benchmarks()
