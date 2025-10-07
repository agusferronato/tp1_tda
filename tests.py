from utils.files import get_expected_results, get_file_info, ls, FILES_PATH
import re 
from tp2 import algorithm
from utils.tests_format import tests_format



def tests():
    _, eliminated_troops_expected = get_expected_results()

    for file_name in ls(FILES_PATH):
        if re.match(r'^\d', file_name):
            xi, f = get_file_info(f'{FILES_PATH}/{file_name}')
            eliminated_troops, strategy = algorithm(xi, f)
            tests_format(file_name, eliminated_troops, eliminated_troops_expected, strategy, xi, f)


if __name__ == "__main__":
    tests()