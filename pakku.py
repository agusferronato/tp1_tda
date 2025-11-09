import heapq


VALUE_POSITION = 1
SET_POSITION = 0
SUM_POSITION = 1


def pakku(masters, k: int):

    result = [[[], 0] for _ in range(k)]

    heap = []
    heapq.heapify(heap)

    for i in range(k):
        heapq.heappush(heap, [0, i])

    masters = sorted(masters, key=lambda master: master[VALUE_POSITION], reverse=True)

    for master in masters:

        _, index = heapq.heappop(heap)

        result[index][SET_POSITION].append(master)
        result[index][SUM_POSITION] += master[VALUE_POSITION]

        heapq.heappush(heap, [(result[index][VALUE_POSITION]) ** 2, index])

    return result
