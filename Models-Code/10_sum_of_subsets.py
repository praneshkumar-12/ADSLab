def sum_of_subsets(arr, target):
    result = []  # List to store all possible solutions
    subset = []  # List to store the current subset
    find_subsets(arr, target, 0, subset, result)
    print_solutions(result)
    return result

def find_subsets(arr, target, index, subset, result):
    # Base case: if the target is reached, add the subset to the result
    if target == 0:
        result.append(subset[:])  # Append a copy of the current subset
        return
    
    # If the target becomes negative, no need to proceed further
    if target < 0:
        return
    
    # Try all elements starting from the current index
    for i in range(index, len(arr)):
        # Include the current element in the subset
        subset.append(arr[i])
        # Recur with the remaining elements and reduced target
        find_subsets(arr, target - arr[i], i + 1, subset, result)
        # Backtrack by removing the current element from the subset
        subset.pop()

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

# Example usage:
arr = [10, 7, 5, 18, 12, 20, 15]  # The given set
target = 35  # The target sum
solutions = sum_of_subsets(arr, target)
print(f"Total number of solutions: {len(solutions)}")
