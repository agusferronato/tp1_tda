import os
import random
import numpy as np 


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SETS_PATH = os.path.join(SCRIPT_DIR, "../sets")
os.makedirs(SETS_PATH, exist_ok=True)

MAX_SIZE = 10000

MIN_F_NUMBER = 50
MAX_F_NUMBER = 2000

MIN_XI_NUMBER = 100
MAX_XI_NUMBER = 1000


def generate_random_arr (size, min_value, max_value):
    arr = []
    for i in range(size):
        arr.append(random.randint(min_value, max_value))
    return arr


def convert_to_file_format (arr):
    return [ f'{elem}\n' for elem in arr ]


def generate_xi (size):
    arr = generate_random_arr(size, MIN_XI_NUMBER, MAX_XI_NUMBER)
    return convert_to_file_format(arr)


def generate_f (size):
    # arr = [int(np.log(i)) for i in range(1, size + 1)]
    arr = sorted(generate_random_arr(size, MIN_F_NUMBER, MAX_F_NUMBER))
    return convert_to_file_format(arr)


# The dataset has the same structure as the files specified in /files
def generate_data_set (size, path=SETS_PATH, index=""):

    with open(f'{path}/{size}{index}.txt', "w") as file:
        
        file.write("\n") # header
        file.write(f'{size}\n') 
        file.writelines(generate_xi(size))
        file.writelines(generate_f(size))



if __name__ == "__main__":
    for i in range(500, MAX_SIZE, 1000):
        generate_data_set(i)