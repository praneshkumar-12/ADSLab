import heapq

# Define a class to represent an item in the knapsack
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

# Define a class to represent a node in the search tree
class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound

# Calculate the upper bound of the node's value
def bound(node, n, capacity, items):
    if node.weight >= capacity:
        return 0

    profit_bound = node.value
    j = node.level + 1
    totweight = node.weight

    # Calculate the bound by adding items until the capacity is reached
    while j < n and totweight + items[j].weight <= capacity:
        totweight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # If there are still items left, calculate the bound by adding a fraction of the next item
    if j < n:
        profit_bound += (capacity - totweight) * items[j].ratio

    return profit_bound

# Solve the knapsack problem using Branch and Bound algorithm
def knapsack(items, capacity):
    # Sort the items based on their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    n = len(items)

    # Create a priority queue to store nodes
    queue = []
    u = Node(-1, 0, 0, 0)
    v = Node(0, 0, 0, 0)
    u.bound = bound(u, n, capacity, items)
    heapq.heappush(queue, u)

    max_value = 0

    # Explore nodes in the priority queue until it is empty
    while queue:
        u = heapq.heappop(queue)

        # If the bound of the node is greater than the current maximum value, explore its children
        if u.bound > max_value:
            v.level = u.level + 1
            v.weight = u.weight + items[v.level].weight
            v.value = u.value + items[v.level].value

            # If the child node is feasible and has a higher value, update the maximum value
            if v.weight <= capacity and v.value > max_value:
                max_value = v.value

            v.bound = bound(v, n, capacity, items)

            # If the bound of the child node is greater than the current maximum value, add it to the queue
            if v.bound > max_value:
                heapq.heappush(queue, Node(v.level, v.value, v.weight, v.bound))

            v.weight = u.weight
            v.value = u.value
            v.bound = bound(v, n, capacity, items)

            # If the bound of the child node is greater than the current maximum value, add it to the queue
            if v.bound > max_value:
                heapq.heappush(queue, Node(v.level, v.value, v.weight, v.bound))

    return max_value

# Run the knapsack algorithm with sample data
if __name__ == "__main__":
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50
    max_value = knapsack(items, capacity)
    print(f"Maximum value in Knapsack = {max_value}")
