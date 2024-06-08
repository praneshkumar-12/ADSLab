class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices in the graph
        self.graph = []  # List to store the edges of the graph

    def add_edge(self, source, destn, cost):
        self.graph.append([source, destn, cost])  # Add an edge to the graph

    def find(self, parent, i):
        # Recursive function to find the parent of a node
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:  # If rank of x is less than rank of y
            parent[x] = y  # Make y as the parent of x
        elif rank[x] > rank[y]:  # If rank of x is greater than rank of y
            parent[y] = x  # Make x as the parent of y
        else:  # If ranks are equal
            parent[y] = x  # Make x as the parent of y
            rank[x] += 1  # Increment the rank of x

    def kruskalMST(self):
        result = []  # List to store the edges of the Minimum Spanning Tree (MST)

        i = 0  # Counter for iterating the graph
        e = 0  # Counter for number of edges generated in MST

        self.graph = sorted(self.graph, key=lambda x: x[2])  # Sort the edges based on their cost

        parent = []  # List to store the parent of each node
        rank = []  # List to store the rank of each node

        for node in range(self.V):
            parent.append(node)  # Initially, parent of each node is itself
            rank.append(0)  # Initially, rank of each node is 0

        while e < self.V - 1:  # For a graph with n vertices, MST contains n - 1 edges
            source, destn, cost = self.graph[i]  # Get the next edge from the sorted graph
            i += 1

            source_parent = self.find(parent, source)  # Find the parent of the source node
            destn_parent = self.find(parent, destn)  # Find the parent of the destination node

            if source_parent != destn_parent:
                # If the parents are different, they belong to different sets, so no cycle is formed
                # An edge can be drawn between the source and destination nodes
                e += 1
                result.append((source, destn, cost))  # Add the edge to the MST

                # As an edge is drawn between source and destination, perform union to make them part of the same set
                self.union(parent, rank, source_parent, destn_parent)

        minimum_cost = 0
        print("Edges in MST:")
        for source, destn, cost in result:
            minimum_cost += cost
            print(f"{source} --> {destn} ==> {cost}")  # Print the edges in the MST

        print("Minimum Cost:", minimum_cost)  # Print the minimum cost of the MST


graph = {
    0: {
        1: 2799,
        2: 713,
        3: 1631,
        4: 2426,
    },
    1: {
        0: 2799,
        2: 2015,
        3: 1547,
        4: 373,
    },
    2: {
        0: 713,
        1: 2015,
        3: 1086,
        4: 1446,
    },
    3: {
        0: 1631,
        1: 1547,
        2: 1086,
        4: 1180,
    },
    4: {
        0: 2426,
        1: 373,
        2: 1446,
        3: 1180,
    },
}

# Assuming you have already defined the Graph class and its methods

# Initialize your graph instance
g = Graph(len(graph))

# Iterate over each key in the graph dictionary
for vertex in graph:
    # Iterate over each adjacent vertex along with its weight
    for adjacent_vertex, weight in graph[vertex].items():
        # Add the edge to the graph
        g.add_edge(vertex, adjacent_vertex, weight)

g.kruskalMST()
