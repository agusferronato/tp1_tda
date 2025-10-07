LINES = 30
MAX_ELEMENTS_SEQUENCE = 50
WAIT = "Cargar"
ATTACK = "Atacar"


def valid_strategy (strategy, eliminated_troops, xi, f):
    wait = 0
    value = 0

    for i in range(len(xi)):
        if strategy[i] == WAIT:
            wait += 1
        else:
            value += min(xi[i], f[wait])
            wait = 0

    return eliminated_troops == value



def tests_format (file_name, eliminated_troops, eliminated_troops_expected, strategy, xi, f):
    print("-" * LINES)
    print(f'\033[1mFile: {file_name}\033[0m')

    print("-" * LINES)
    print("\033[1mTroops eliminated\033[0m")
    print(f'Obtained value: {eliminated_troops}')
    print(f'Expected value: {eliminated_troops_expected[file_name]}')



    print("-" * LINES)
    print("\033[1mSequence\033[0m")

    if len(strategy) > MAX_ELEMENTS_SEQUENCE:
        print(f'Obtained sequence: {strategy[:MAX_ELEMENTS_SEQUENCE]} ...')
    else:
        print(f'Obtained sequence: {strategy}')


    if eliminated_troops == eliminated_troops_expected[file_name] and valid_strategy(strategy, eliminated_troops, xi, f):
        print("\033[1m\033[32m✅​ Passed\033[0m")
    else:
        print("\033[1m\033[31m❌​ Failed\033[0m")

    print()