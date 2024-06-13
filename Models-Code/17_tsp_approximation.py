# Program to solve Traveling Salesman Problem using Approximation.

import math

def tsp_approximation(points):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    n = len(points)
    visited = [False] * n
    path = []
    total_distance = 0

    current = 0
    path.append(current)
    visited[current] = True

    for _ in range(1, n):
        next_point = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i]:
                dist = distance(points[current], points[i])
                if dist < min_dist:
                    min_dist = dist
                    next_point = i
        current = next_point
        path.append(current)
        visited[current] = True
        total_distance += min_dist

    # Return to the starting point
    total_distance += distance(points[path[-1]], points[path[0]])
    path.append(path[0])

    return path, total_distance

# Example usage:
points = [(0, 0), (1, 1), (2, 2), (0, 2)]
path, dist = tsp_approximation(points)
print(f"Approximate TSP path: {path} with total distance: {dist}")

