LINES = 30
MAX_ELEMENTS_SEQUENCE = 50


def find_first_mismatch (strategy, sequence_expected):

    for i in range(1, len(strategy)):
        if strategy[i] != sequence_expected[i]:
            print(f"\033[1m\033[31mAt element {i}. Expected value: {sequence_expected[i]}. Obtained value: {strategy[i]}\033[0m")





def tests_format (file_name, eliminated_troops, eliminated_troops_expected, strategy, sequence_expected):
    print("-" * LINES)
    print(f'\033[1mFile: {file_name}\033[0m')

    print("-" * LINES)
    print("\033[1mTroops eliminated\033[0m")
    print(f'Obtained value: {eliminated_troops}')
    print(f'Expected value: {eliminated_troops_expected[file_name]}')


    print("-" * LINES)
    print("\033[1mSequence\033[0m")
    if len(strategy) > MAX_ELEMENTS_SEQUENCE:
        print(f'Obtained value: {strategy[:MAX_ELEMENTS_SEQUENCE]} ...')
        print(f'Expected value: {sequence_expected[file_name][:MAX_ELEMENTS_SEQUENCE]} ...')
    else:
        print(f'Obtained value: {strategy}')
        print(f'Expected value: {sequence_expected[file_name]}')


    same_strategy = strategy == sequence_expected[file_name]
    if eliminated_troops == eliminated_troops_expected[file_name] and same_strategy:
        print("\033[1m\033[32m✅​ Passed\033[0m")
    else:
        print("\033[1m\033[31m❌​ Failed\033[0m")
        if not same_strategy:
            print()
            find_first_mismatch(strategy, sequence_expected[file_name])

    print()