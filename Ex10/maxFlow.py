from collections import deque

def bfs_capacity_path(capacity, source, sink, parent):
    """
    Perform a Breadth-First Search to find an augmenting path from source to sink.
    """
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, cap in enumerate(capacity[u]):
            if not visited[v] and cap > 0:  # If the vertex is not visited and the capacity is positive
                queue.append(v)
                visited[v] = True
                parent[v] = u

                if v == sink:
                    return True

    return False

def ford_fulkerson(capacity, source, sink):
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow in a flow network.
    """
    parent = [-1] * len(capacity)
    max_flow = 0

    while bfs_capacity_path(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

# Example usage
capacity = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink = 5

max_flow = ford_fulkerson(capacity, source, sink)
print(f"The maximum possible flow is {max_flow}")
