VALUE_POSITION = 1
NAME_POSITION = 0
Master = tuple[str, int] 


def score(groups, k: int) -> int:
    result: int = 0
    for i in range(k):
        current_group = sum(master[VALUE_POSITION] for master in groups[i])
        result += current_group**2

    return result
