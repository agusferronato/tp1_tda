import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tp3 import algorithm as bt
from algorithms.greedy import pakku
from algorithms.lineal_programming import (
    approximate_linear_programming as alp,
    linear_programming as lp,
)
from tabulate import tabulate
from utils.generate_data_sets import generate_random_data_sets, generate_alternative_ds, EXPECTED_RESULTS_PATH, FOLDER
from utils.files import get_file_info, get_expected_results


MIN_SIZE = 201
MAX_SIZE = 300
STEP = 2


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

    for size in range(MIN_SIZE, MAX_SIZE, STEP):
        
        k = size // 2

        generate_alternative_ds(size, k)

    optimal_value = get_expected_results(EXPECTED_RESULTS_PATH)

    for size in range(MIN_SIZE, MAX_SIZE, STEP):

        k = size // 2

        file = f"{size}_{k}.txt"
        masters, _ = get_file_info(f"{FOLDER}/{file}")

        for algorithm in [pakku]:

            print(f"a: {name[algorithm]}, size: {size}, k: {k}")

            if size not in results[algorithm]:
                results[algorithm][size] = {}

            results[algorithm][size][k] = []

            start = time.time()

            value = algorithm(masters, k)
            if isinstance(value, tuple):
                value = value[0]

            ratio = value / optimal_value[file]
            expected_max_ratio = 1.0 + (1/(9.0*k)) - (1/(9.0*k**2))
            is_expected_ratio = ratio <= expected_max_ratio

            results[algorithm][size][k].append([time.time() - start, ratio, expected_max_ratio, is_expected_ratio])


    times_data = {}
    ratio_data = {}
    expected_max_ratio = {}
    is_expected_ratio = {}



    for algorithm, sizes in results.items():
        for size, ks in sizes.items():        
            for k, records in ks.items():     

                key = f"n={size}, k={k}"

                if key not in expected_max_ratio:
                    expected_max_ratio[key] = []
                if key not in is_expected_ratio:
                    is_expected_ratio[key] = []
                if key not in times_data:
                    times_data[key] = []
                if key not in ratio_data:
                    ratio_data[key] = []

                for record in records:                    
                    total_time, ratio, max_ratio, expected_ratio_matches = record
                    times_data[key].append([total_time])
                    ratio_data[key].append([ratio])
                    expected_max_ratio[key].append([max_ratio])
                    is_expected_ratio[key].append([expected_ratio_matches])


    """
    headers = [name[algorithm] for algorithm in [alp, lp, bt, pakku]]

    values_data = [[k, *v] for k, v in values_data.items()]
    times_data = [[k, *v] for k, v in times_data.items()]
    ratio_data = [[k, *v] for k, v in ratio_data.items()]

    print(tabulate(values_data, headers=headers, tablefmt="grid"))
    print(tabulate(times_data, headers=headers, tablefmt="grid"))
    print(tabulate(ratio_data, headers=headers, tablefmt="grid"))
    """

    headers = ["n", "Execution time (s)", "Ratio (SOL/OPT)", "Max ratio", "Ratio <= Max ratio"]
    rows = []

    for algorithm, sizes in results.items():
        for size, ks in sizes.items():
            for k, records in ks.items():
                key = f"n={size}, k={k}"
                rows.append([size, times_data[key], ratio_data[key], expected_max_ratio[key], is_expected_ratio[key][0]])

    print(tabulate(rows, headers=headers, tablefmt="grid"))



if __name__ == "__main__":
    compare_algorithms()