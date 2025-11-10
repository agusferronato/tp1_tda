import copy
from utils.problem import VALUE_POSITION, Master


def bt(masters: list[Master], k: int, index: int, current, best):

    sum_of_each_set, current_list, current_sum = current
    best_sum, best_list = best

    if len(masters) == index:
        if current_sum < best_sum:
            return current_sum, copy.deepcopy(current_list)

    if current_sum >= best_sum:
        return best_sum, best_list

    master = masters[index]
    master_value = master[VALUE_POSITION]
    visited_values = set()

    for i in range(k):
        if sum_of_each_set[i] in visited_values:
            continue

        visited_values.add(sum_of_each_set[i])

        current_list[i].append(master)

        current_sum -= sum_of_each_set[i] ** 2
        sum_of_each_set[i] += master_value
        current_sum += sum_of_each_set[i] ** 2

        current = (sum_of_each_set, current_list, current_sum)
        best = bt(masters, k, index + 1, current, best)

        current_sum -= sum_of_each_set[i] ** 2
        sum_of_each_set[i] -= master_value
        current_sum += sum_of_each_set[i] ** 2

        current_list[i].pop()

    return best


def bt_2(masters: list[Master], k: int, index: int, current, best):

    sum_of_each_set, current_list, current_sum, remains = current
    best_sum, best_list = best

    if len(masters) == index:
        if current_sum < best_sum:
            return current_sum, copy.deepcopy(current_list)

    if lower_bound(sum_of_each_set, remains) >= best_sum:
        return best_sum, best_list

    master = masters[index]
    master_value = master[VALUE_POSITION]
    visited_values = set()

    for i in range(k):
        if sum_of_each_set[i] in visited_values:
            continue

        visited_values.add(sum_of_each_set[i])

        current_list[i].append(master)

        remains -= master_value
        current_sum -= sum_of_each_set[i] ** 2
        sum_of_each_set[i] += master_value
        current_sum += sum_of_each_set[i] ** 2

        current = (sum_of_each_set, current_list, current_sum, remains)
        best = bt_2(masters, k, index + 1, current, best)

        remains += master_value
        current_sum -= sum_of_each_set[i] ** 2
        sum_of_each_set[i] -= master_value
        current_sum += sum_of_each_set[i] ** 2

        current_list[i].pop()

    return best


def lower_bound(sum_of_each_set: list[int], remains: int) -> int:
    sums = sorted(sum_of_each_set)
    k = len(sums)

    for i in range(k - 1):
        if remains == 0:
            break
        diff = sums[i + 1] - sums[i]
        block = i + 1
        need = diff * block
        if remains >= need:
            for j in range(block):
                sums[j] += diff
            remains -= need
        else:
            full = remains // block
            rest = remains % block
            for j in range(block):
                sums[j] += full
            for j in range(rest):
                sums[j] += 1
            remains = 0
    if remains > 0:
        full = remains // k
        rest = remains % k
        for i in range(k):
            sums[i] += full
        for i in range(rest):
            sums[i] += 1

    return sum(s ** 2 for s in sums)
