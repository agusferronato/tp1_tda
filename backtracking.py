import copy

VALUE_POSITION = 1

def bt (masters, k, index, current, best):

    sum_of_each_set, current_list, current_sum = current
    best_sum, best_list = best 
    
    if len(masters) == index:
        if current_sum < best_sum:
            return current_sum, copy.deepcopy(current_list)

    if current_sum >= best_sum:
        return best_sum, best_list


    master = masters[index]
    master_value = master[VALUE_POSITION] 
    visited_values = set()


    for i in range(k):
        if sum_of_each_set[i] in visited_values:
            continue

        visited_values.add(sum_of_each_set[i])

        current_list[i].append(master)

        current_sum -= sum_of_each_set[i] ** 2
        sum_of_each_set[i] += master_value
        current_sum += sum_of_each_set[i] ** 2


        best = bt(masters, k, index + 1, (sum_of_each_set, current_list, current_sum), best)
            
        current_sum -= sum_of_each_set[i] ** 2
        sum_of_each_set[i] -= master_value
        current_sum += sum_of_each_set[i] ** 2

        current_list[i].pop()        

    return best