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

    return OPT[n], [] 


if __name__ == "__main__":
    pass 