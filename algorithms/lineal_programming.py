import pulp
from utils.problem import VALUE_POSITION


def linear_programming(masters, k):

    n = len(masters)
    masters.sort(key=lambda master: master[VALUE_POSITION])
    M = pulp.LpVariable.dicts("M", (range(n), range(k)), cat="Binary")
    E = pulp.LpVariable.dicts("E", (range(n), range(n), range(k)), cat="Binary")

    problem = pulp.LpProblem("PTA", pulp.LpMinimize)

    for i in range(n):
        problem += pulp.lpSum(M[i][j] for j in range(k)) == 1

    for i in range(n):
        for m in range(i + 1, n):
            for j in range(k):
                problem += M[i][j] + M[m][j] >= 2 * E[i][m][j]
                problem += M[i][j] + M[m][j] <= 1 + E[i][m][j]

    for i in range(k-1):
        problem += pulp.lpSum(M[m][i] for m in range(n)) <= pulp.lpSum(M[m][i+1] for m in range(n))

    problem += pulp.lpSum(
        2 * E[i][m][j] * masters[i][VALUE_POSITION] * masters[m][VALUE_POSITION]
        for i in range(n)
        for m in range(i + 1, n)
        for j in range(k)
    ) + sum(master[VALUE_POSITION] ** 2 for master in masters)

    problem.solve(pulp.PULP_CBC_CMD(threads=8, msg=False))

    return int(pulp.value(problem.objective))


def approximate_linear_programming(masters, k):

    n = len(masters)
    M = pulp.LpVariable.dicts("M", (range(n), range(k)), cat="Binary")
    S = pulp.LpVariable.dicts("S", (range(k)), cat="Binary")
    major = pulp.LpVariable("W", cat="Binary")
    minor = pulp.LpVariable("m", cat="Binary")

    problem = pulp.LpProblem("PTA", pulp.LpMinimize)

    for i in range(n):
        problem += pulp.lpSum(M[i][j] for j in range(k)) == 1

    for j in range(k):
        S[j] == pulp.lpSum(M[i][j] * masters[i][VALUE_POSITION] for i in range(n))
        problem += major >= S[j]
        problem += minor <= S[j]

    problem += major - minor

    problem.solve(pulp.PULP_CBC_CMD(threads=8, msg=False))

    set_sum = 0
    for j in range(k):  
        set_sum += sum(masters[i][VALUE_POSITION] * M[i][j].value() for i in range(n)) ** 2
    return set_sum

    