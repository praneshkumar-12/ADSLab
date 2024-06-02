# Definition of the Graph class
class Graph:
    def __init__(self, vertices):
        # Number of vertices in the graph
        self.V = vertices
        # List to store all the edges in the graph
        self.graph = []
    
    # Method to add an edge to the graph
    def add_edge(self, u, v, w):
        # Append the edge (u, v) with weight w to the graph
        self.graph.append([u, v, w])

    # Method to find the root (or representative) of the set that element i is part of
    def find(self, parent, i):
        # If i is not the parent of itself, then it's not the root
        if parent[i] != i:
            # Recursively find the root and apply path compression
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # Method to unite (or merge) two sets containing elements x and y
    def union(self, parent, rank, x, y):
        # Attach the tree with lower rank to the tree with higher rank
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            # If ranks are same, then make one as root and increase its rank by one
            parent[y] = x
            rank[x] += 1
    
    # Method to construct the Minimum Spanning Tree using Kruskal's algorithm
    def kruskalMST(self):
        # This will store the resultant MST
        result = []
        
        # An index variable, used for sorted edges
        i = 0
        # An index variable, used for result[]
        e = 0
        
        # Step 1: Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key = lambda x: x[2])

        # Allocate memory for creating V subsets
        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause a cycle, include it in the result
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        # Print the constructed MST
        minimumCost = 0
        print("Edges constructed in MST:")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        
        print("Minimum cost is", minimumCost)

# Dictionary representation of the graph with cities as vertices and distances as weights
graph = {
    "New York": {
        "Los Angeles": 2799,
        "Chicago": 713,
        "Houston": 1631,
        "Phoenix": 2426,
    },
    "Los Angeles": {
        "New York": 2799,
        "Chicago": 2015,
        "Houston": 1547,
        "Phoenix": 373,
    },
    "Chicago": {
        "New York": 713,
        "Los Angeles": 2015,
        "Houston": 1086,
        "Phoenix": 1446,
    },
    "Houston": {
        "New York": 1631,
        "Los Angeles": 1547,
        "Chicago": 1086,
        "Phoenix": 1180,
    },
    "Phoenix": {
        "New York": 2426,
        "Los Angeles": 373,
        "Chicago": 1446,
        "Houston": 1180,
    },
}

# Initialize the Graph instance with the number of vertices
g = Graph(len(graph))

# Iterate over each key (vertex) in the graph dictionary
for vertex in graph:
    # Iterate over each adjacent vertex and the corresponding weight
    for adjacent_vertex, weight in graph[vertex].items():
        # Add the edge to the graph instance
        g.add_edge(vertex, adjacent_vertex, weight)

# Print the Minimum Spanning Tree and its total weight
print(g.kruskalMST())
