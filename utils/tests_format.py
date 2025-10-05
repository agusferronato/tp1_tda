LINES = 30


def tests_format (file_name, eliminated_troops, eliminated_troops_expected):
    print("-" * LINES)
    print(f'\033[1mFile: {file_name}\033[0m')
    print("-" * LINES)
    print("Troops eliminated")
    print(f'Obtained value: {eliminated_troops}')
    print(f'Expected value: {eliminated_troops_expected[file_name]}')
    if eliminated_troops == eliminated_troops_expected[file_name]:
        print("\033[1m\033[32m✅​ Passed\033[0m")
    else:
        print("\033[1m\033[31m❌​ Failed\033[0m")
    print()