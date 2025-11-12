VALUE_POSITION = 1


def polynomial_verifier(masters, groups, B: int, k: int) -> bool:

    if len(groups) != k:
        return False

    # Verificar que los maestros aparezcan una vez por grupo

    masters_apparences = set()
    for group in groups:
        for master in group:
            if master not in masters_apparences:
                masters_apparences.add(master)
            else:
                return False
            
    if len(masters_apparences) != len(masters):
        return False

    # Verificar que todos los maestros esten en el conjunto original

    for group in groups:
        for master in group:
            if master not in masters:
                return False

    # Verificar si la suma de los cuadrados no excede B

    total = 0

    for group in groups:
        group_sum = 0
        for master in group:
            group_sum += master[VALUE_POSITION]
        total += group_sum ** 2
        if total > B:
            return False

    return True


def polynomial_verifier_2_partition (S, S_1, S_2 : set):

    if len(S_1) + len(S_2) != len(S):
        return False
    
    # Verifico si todo elemento de S_1 no esta en S_2 (y viceversa) y si pertenecen todos a S

    for x in S_1:
        if x in S_2 or x not in S:
            return False
        
    # Verifico si los elementos de S_2 pertenecen a S

    for x in S_2:
        if x not in S:
            return False

    if S_2.union(S_1) != S:
        return False


    return sum(S_1) == sum(S_2)
    