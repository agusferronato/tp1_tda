import heapq
from utils.problem import VALUE_POSITION, score, Master
import random

RESTARTS: int = 1000


def greedy(masters: list[Master], k: int):
    sums: list[int] = [0] * k

    heap = [(0, i) for i in range(k)]
    group: list = [[] for _ in range(k)]

    heapq.heapify(heap)

    for master in masters:

        current_sum, i = heapq.heappop(heap)
        group[i].append(master)

        new_sum = current_sum + master[VALUE_POSITION]
        heapq.heappush(heap, (new_sum, i))

        sums[i] = new_sum

    return score(group, k), group


def pakku(masters: list[Master], k: int):
    masters = sorted(masters, key=lambda master: master[VALUE_POSITION], reverse=True)
    return greedy(masters, k)


def approximate(masters: list[Master], k: int):
    if k >= len(masters):
        groups = [[master] for master in masters]
        return score(groups, k), groups
    elif k == 1:
        return score([masters], k), [masters]

    ordered = sorted(masters, key=lambda m: m[VALUE_POSITION], reverse=True)
    best_sum, best_group = pakku(masters, k)

    # multi-start
    for r in range(RESTARTS):
        if r > 0:
            random.shuffle(ordered)
        current_sum, groups = greedy(ordered, k)
        if current_sum < best_sum:
            best_sum = current_sum
            best_group = [list(g) for g in groups]

    return best_sum, best_group
