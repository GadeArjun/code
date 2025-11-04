def fraction_knapsack(weight, value, capacity):
    items = []
    for i in range(len(weight)):
        ratio = value[i] / weight[i]
        items.append((ratio,weight[i],value[i]))

    items.sort(reverse=True)

    remaining_capacity = capacity
    total_value = 0

    for ratio, weight, value in items:

        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_value += fraction * value
            remaining_capacity = 0
    return total_value





weight = list(map(int, input("NEnter Weight: ").split()))
value = list(map(int, input("NEnter Value: ").split()))
capacity = int(input("NEnter capacity: "))

max_val = fraction_knapsack(weight, value, capacity)
print(max_val)


