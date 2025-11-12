import pulp

VALUE_POSITION = 1

def linear_programming(masters, k):

    M_ij = []  # El maestro i esta en el grupo j
    E_mkj = []  # Los maestros m y k estan en el grupo j

    for i in range(len(masters)):
        for j in range(k):
            M_ij.append(pulp.LpVariable(f"M_{i}_{j}", cat="Binary"))

    for i in range(len(masters)):
        for j in range(len(masters)):
            for m in range(k):
                E_mkj.append(pulp.LpVariable(f"E_{i}_{j}_{m}", cat="Binary"))

    problem = pulp.LpProblem("PTA", pulp.LpMinimize)

    for i in range(len(masters)):
        problem += pulp.lpSum([M_ij[i * k + j] for j in range(k)]) == 1

    for i in range(len(masters)):
        for j in range(len(masters)):
            for m in range(k):
                problem += (
                    M_ij[i * k + m] + M_ij[j * k + m]
                    >= 2 * E_mkj[(i * len(masters) + j) * k + m]
                )
                problem += (
                    M_ij[i * k + m] + M_ij[j * k + m]
                    <= 1 + E_mkj[(i * len(masters) + j) * k + m]
                )

    problem += pulp.lpSum(
        E_mkj[(i * len(masters) + j) * k + m]
        * masters[i][VALUE_POSITION]
        * masters[j][VALUE_POSITION]
        for i in range(len(masters))
        for j in range(len(masters))
        for m in range(k)
    )

    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(problem.objective))



def linear_programming_optimized(masters, k):

    n = len(masters)

    M_ij = [[] for _ in range(n)]  # El maestro i esta en el grupo j

    # Los maestros i y m estan en el grupo j
    E_imj = [
        [
            [pulp.LpVariable(f"E_{i}_{m}_{j}", cat="Binary") for j in range(k)]
            for m in range(i + 1, n)
        ]
        for i in range(n)
    ]

    for i in range(n):
        for j in range(k):
            M_ij[i].append(pulp.LpVariable(f"M_{i}_{j}", cat="Binary"))

    problem = pulp.LpProblem("PTA", pulp.LpMinimize)

    for i in range(n):
        problem += pulp.lpSum([M_ij[i][j] for j in range(k)]) == 1

    for i in range(n):
        for m in range(i + 1, n):
            for j in range(k):
                problem += M_ij[i][j] + M_ij[m][j] >= 2 * E_imj[i][m - i - 1][j]
                problem += M_ij[i][j] + M_ij[m][j] <= 1 + E_imj[i][m - i - 1][j]

    problem += pulp.lpSum(
        2
        * E_imj[i][m - i - 1][j]
        * masters[i][VALUE_POSITION]
        * masters[m][VALUE_POSITION]
        for i in range(n)
        for m in range(i + 1, n)
        for j in range(k)
    ) + sum(master[VALUE_POSITION] ** 2 for master in masters)

    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(problem.objective))
