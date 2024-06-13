# Knapsack using Approximation algorithm


def knapsack_approximation(values, weights, capacity):
    n = len(values)
    value_per_weight = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    value_per_weight.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    total_weight = 0

    for v_pw, value, weight in value_per_weight:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
        else:
            remain_capacity = capacity - total_weight
            total_value += value * (remain_capacity / weight)
            break

    return total_value

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(f"Approximate knapsack solution: {knapsack_approximation(values, weights, capacity)}")
