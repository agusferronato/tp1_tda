import pulp
from utils.problem import VALUE_POSITION


def linear_programming(masters, k):

    n = len(masters)
    
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


    problem += pulp.lpSum(
        2 * E[i][m][j] * masters[i][VALUE_POSITION] * masters[m][VALUE_POSITION]
        for i in range(n)
        for m in range(i + 1, n)
        for j in range(k)
    ) + sum(master[VALUE_POSITION] ** 2 for master in masters)
    
    problem.solve(pulp.PULP_CBC_CMD(threads=8, msg=False))

    return int(pulp.value(problem.objective))
