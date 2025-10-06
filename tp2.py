

def reconstruction (xi, f, OPT):

    index = len(xi)
    solution = []

    while index > 0:
        for j in range(1, index + 1):
            if OPT[index] == OPT[index - j] + min(f[j - 1], xi[index - 1]):
                solution.append("Atacar")
                solution.extend(["Cargar"] * (j - 1))
                index -= j
                break  

    solution.reverse()
    return solution



def algorithm (xi, f):

    n = len(xi)
    OPT = [0] * (n + 1)

    for i in range(1, n + 1):
        max_value = -1
        for j in range(1, i + 1):
            current_value = OPT[i - j] + min(f[j - 1], xi[i - 1])
            if max_value < current_value:
                max_value = current_value
        OPT[i] = max_value   

    return OPT[n], reconstruction(xi, f, OPT) 


if __name__ == "__main__":
    pass 