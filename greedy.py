import heapq
from utils.problem import VALUE_POSITION, score, Master


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

    return group


def a(masters: list[Master], k: int):
    # aca hacemos nuestra mejor aproximacion
    # la idea es refinar pakku o usar greedy de otra forma asi tarda menos bt
    return


def pakku(masters: list[Master], k: int):
    masters = sorted(masters, key=lambda master: master[VALUE_POSITION], reverse=True)
    return greedy(masters, k)
