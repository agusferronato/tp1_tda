VALUE_POSITION = 1

def polynomial_verifier(masters, groups, B, k):

    if len(groups) != k:
        return False

    for group in groups:
        for master in group:
            if master not in masters:
                return False
    
    total = 0

    for group in groups:
        group_sum = 0
        for master in group:
            group_sum += master[VALUE_POSITION]
        total += group_sum ** 2
        if total > B:
            return False
    
    return True
    

