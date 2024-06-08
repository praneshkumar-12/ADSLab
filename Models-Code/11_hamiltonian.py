def hamiltonian_cycle(adj_matrix):
    n = len(adj_matrix)  # Number of vertices in the graph
    path = [-1] * n  # To store the Hamiltonian Cycle path
    result = []  # List to store all possible Hamiltonian Cycles

    # Start from the first vertex
    path[0] = 0
    find_hamiltonian_cycle(adj_matrix, path, 1, result)
    
    print_solutions(result)
    return result

def find_hamiltonian_cycle(adj_matrix, path, pos, result):
    # Base case: If all vertices are included in the path
    if pos == len(adj_matrix):
        # And if there is an edge from the last vertex to the first vertex
        if adj_matrix[path[pos - 1]][path[0]] == 1:
            result.append(path[:])  # Append a copy of the current path to result
        return
    
    # Try different vertices as the next candidate in Hamiltonian Cycle
    for v in range(1, len(adj_matrix)):
        if is_safe(v, adj_matrix, path, pos):
            path[pos] = v
            find_hamiltonian_cycle(adj_matrix, path, pos + 1, result)
            path[pos] = -1  # Backtrack

def is_safe(v, adj_matrix, path, pos):
    # Check if this vertex is an adjacent vertex of the previously added vertex
    if adj_matrix[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included
    if v in path:
        return False

    return True

def print_solutions(solutions):
    for solution in solutions:
        print(solution + [solution[0]])  # Print the cycle by returning to the start vertex

# Example usage:
adj_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]  # Adjacency matrix of the graph

solutions = hamiltonian_cycle(adj_matrix)
print(f"Total number of solutions: {len(solutions)}")
