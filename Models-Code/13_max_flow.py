from collections import deque

def bfs_capacity_path(capacity, source, sink, parent):
    """
    Perform a Breadth-First Search to find an augmenting path from source to sink.
    """
    visited = [False] * len(capacity)  # Create a list to keep track of visited vertices
    queue = deque([source])  # Create a queue and enqueue the source vertex
    visited[source] = True  # Mark the source vertex as visited

    while queue:  # While the queue is not empty
        u = queue.popleft()  # Dequeue a vertex from the queue

        for v, cap in enumerate(capacity[u]):  # Iterate over the neighbors of the dequeued vertex
            if not visited[v] and cap > 0:  # If the vertex is not visited and the capacity is positive
                queue.append(v)  # Enqueue the neighbor vertex
                visited[v] = True  # Mark the neighbor vertex as visited
                parent[v] = u  # Set the parent of the neighbor vertex as the dequeued vertex

                if v == sink:  # If the sink vertex is reached, return True
                    return True

    return False  # If the sink vertex is not reached, return False

def ford_fulkerson(capacity, source, sink):
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow in a flow network.
    """
    parent = [-1] * len(capacity)  # Create a list to keep track of the parent of each vertex
    max_flow = 0  # Initialize the maximum flow as 0

    while bfs_capacity_path(capacity, source, sink, parent):  # While there is an augmenting path from source to sink
        path_flow = float('Inf')  # Initialize the path flow as infinity
        s = sink

        while s != source:  # Traverse the augmenting path from sink to source
            path_flow = min(path_flow, capacity[parent[s]][s])  # Update the path flow with the minimum capacity of the edges
            s = parent[s]  # Move to the parent vertex

        v = sink
        while v != source:  # Traverse the augmenting path from sink to source
            u = parent[v]  # Get the parent vertex
            capacity[u][v] -= path_flow  # Reduce the capacity of the forward edge
            capacity[v][u] += path_flow  # Increase the capacity of the backward edge
            v = parent[v]  # Move to the parent vertex

        max_flow += path_flow  # Update the maximum flow

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

max_flow = ford_fulkerson(capacity, source, sink)  # Find the maximum flow using the Ford-Fulkerson algorithm
print(f"The maximum possible flow is {max_flow}")  # Print the maximum flow
