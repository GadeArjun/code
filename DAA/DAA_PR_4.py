# not optimize

def knasack_01(weight, value, capacity):

    items = []
    for i in range(len(weight)):
        ratio = value[i] / weight[i]
        items.append((ratio, weight[i], value[i]))
    
    items.sort(reverse=True)

    remaining_capacity = capacity
    total_value = 0.0

    for ratio, weight, value in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            remaining_capacity -= weight
            total_value += value
    return total_value


weight = list(map(int, input("Enter Weight: ").split()))
value = list(map(int, input("Enter Value: ").split()))
capacity = int(input("Enter Capacity: "))

max_value = knasack_01(weight, value, capacity)
print(max_value)
