import sys
import math
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tp3 import algorithm as bt
from algorithms.greedy import pakku, approximate
from algorithms.lineal_programming import (
    approximate_linear_programming as alp,
    linear_programming as lp,
)
from tabulate import tabulate
from utils.generate_data_sets import generate_worst_pakku, EXPECTED_RESULTS_PAKKU_PATH, PAKKU_DATA_SETS
from utils.files import get_file_info, get_expected_results



MIN_K = 2000
MAX_K = 15001
STEP = 500


def compare_algorithms():

    results = {}
    name = {
        alp: "Approximate Lineal Programming",
        lp: "Lineal Programming",
        bt: "Backtracking",
        pakku: "Pakku",
    }

    for algorithm in [pakku]:
        results[algorithm] = {}


    for k in range(MIN_K, MAX_K, STEP):
        generate_worst_pakku(k)


    optimal_value = get_expected_results(EXPECTED_RESULTS_PAKKU_PATH)


    for k in range(MIN_K, MAX_K, STEP):

        size = 2*k + 1

        file = f"{size}_{k}.txt"
        masters, _ = get_file_info(f"{PAKKU_DATA_SETS}/{file}")

        for algorithm in [pakku]:

            # print(f"a: {name[algorithm]}, size: {size}, k: {k}")

            if size not in results[algorithm]:
                results[algorithm][size] = {}

            results[algorithm][size][k] = []

            start = time.time()

            value = algorithm(masters, k)
            if isinstance(value, tuple):
                value = value[0]
            
            ratio = value / optimal_value[file]
            expected_ratio = 1.0 + (1.0/(9.0*k)) - (1.0/(9.0*k**2))

            results[algorithm][size][k].append(
                [time.time() - start, ratio, math.isclose(ratio, expected_ratio, rel_tol=1e-12)]
            )

    times_data = {}
    ratio_data = {}
    expected_ratio = {}
    is_expected_ratio = {}
    metrics = [times_data, ratio_data, expected_ratio, is_expected_ratio]

    for algorithm, sizes in results.items():
        for size, ks in sizes.items():
            for k, records in ks.items():

                key = f"n={size}, k={k}"

                for metric in metrics:
                    if key not in metric:
                        metric[key] = []
                    
                for record in records:
                    total_time, ratio, ratio_equal_expected = record
                    times_data[key].append(total_time)
                    ratio_data[key].append(ratio)
                    expected_ratio[key].append(1 + (1/(9*k)) - (1/(9*k**2)))
                    is_expected_ratio[key].append(ratio_equal_expected)


    headers = ["k", "Execution time (s)", "Ratio (SOL/OPT)", "Expected ratio", "Ratio == Expected ratio"]
    rows = []

    for algorithm, sizes in results.items():
        for size, ks in sizes.items():
            for k, records in ks.items():
                key = f"n={size}, k={k}"
                rows.append([k, times_data[key], str(ratio_data[key]), expected_ratio[key], is_expected_ratio[key][0]])

    print(tabulate(rows, headers=headers, tablefmt="grid"))





if __name__ == "__main__":
    compare_algorithms()
