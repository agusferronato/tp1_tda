import pulp
from pulp import LpAffineExpression as Sumatoria

VALUE_POSITION = 1


def clique_maximo(grafo):

    Y = []
    V = len(grafo)
    no_adyacentes = {}
    vertices = grafo.obtener_vertices()

    for i in range(V):
        Y.append(pulp.LpVariable("Y" + str(i), cat="Binary"))
        no_adyacentes[i] = []
        for w in grafo:
            if w not in grafo.adyacentes(vertices[i]) and w != vertices[i]:
                no_adyacentes[i].append(vertices.index(w))

    problem = pulp.LpProblem("Clique max", pulp.LpMaximize)

    for i in range(V):
        problem += pulp.lpSum([ Y[j] for j in no_adyacentes[i] ]) <= (1 - Y[i]) * (V + 1) 

    problem += Sumatoria([(Y[i], 1) for i in range(V)])

    problem.solve()

    resultado = []

    for i in range(V):
        if pulp.value(Y[i]) == 1:
            resultado.append(vertices[i])

    return resultado


def linear_programming(masters, k):

    M_ij = [] # El maestro i esta en el grupo j
    E_mkj = [] # Los maestros m y k estan en el grupo j
    #C_mk = [] # Los maestros m y k estan en el mismo grupo

    for i in range(len(masters)):
        for j in range(k):
            M_ij.append(pulp.LpVariable(f"M_{i}_{j}", cat="Binary"))

    for i in range(len(masters)):
        for j in range(len(masters)):
            for m in range(k):
                E_mkj.append(pulp.LpVariable(f"E_{i}_{j}_{m}", cat="Binary"))

    # for i in range(len(masters)):
    #    for j in range(len(masters)):
    #
    #         C_mk.append(pulp.LpVariable(f"C_{i}_{j}", cat="Binary"))

    problem = pulp.LpProblem("PTA", pulp.LpMinimize)

    for i in range(len(masters)):
        problem += pulp.lpSum([M_ij[i * k + j] for j in range(k)]) == 1

    for i in range(len(masters)):
        for j in range(len(masters)):
            for m in range(k):
                problem += M_ij[i*k + m] + M_ij[j*k + m] >= 2 * E_mkj[(i * len(masters) + j) * k + m]
                problem += M_ij[i*k + m] + M_ij[j*k + m] <= 1 + E_mkj[(i * len(masters) + j) * k + m]

    # for i in range(len(masters)):
    #    for j in range(len(masters)):
    #        problem += C_mk[i*len(masters) + j] == pulp.lpSum([ E_mkj[(i * len(masters) + j) * k + m] for m in range(k) ])


    # problem += pulp.lpSum(
    #    C_mk[i*len(masters) + j] * masters[i][VALUE_POSITION] * masters[j][VALUE_POSITION]
    #    for i in range(len(masters))
    #    for j in range(len(masters))
    #)

    problem += pulp.lpSum(
        E_mkj[(i*len(masters) + j) * k + m] * masters[i][VALUE_POSITION] * masters[j][VALUE_POSITION]
        for i in range(len(masters))
        for j in range(len(masters))
        for m in range(k)

    )

    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(problem.objective))


def linear_programming_2(masters, k):
    n = len(masters)
    M = pulp.LpVariable.dicts("M", (range(k), range(n)), cat="Binary")
    Z = pulp.LpVariable.dicts("Z", (range(k), range(n), range(n)), cat="Binary")

    problem = pulp.LpProblem("PTAgua", pulp.LpMinimize)

    for j in range(len(masters)):
        problem += pulp.lpSum([M[i][j] for i in range(k)]) == 1

    for i in range(k):
        for j in range(len(masters)):
            for r in range(j+1, n):
                problem += Z[i][j][r] <= M[i][j]
                problem += Z[i][j][r] <= M[i][r]
                problem += Z[i][j][r] >= M[i][j] + M[i][r] - 1

    objective_terms = []

    for i in range(k):
        objective_terms += [masters[j][VALUE_POSITION] ** 2 * M[i][j] for j in range(n)]
        objective_terms += [2 * masters[j][VALUE_POSITION] * masters[r][VALUE_POSITION] * Z[i][j][r] for j in range(n) for r in range(j+1, n)]

    problem += pulp.lpSum(objective_terms)

    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(problem.objective))
