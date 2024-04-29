class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    
    def kruskalMST(self):
        result = []

        i = 0
        e = 0

        self.graph = sorted(self.graph, key = lambda x:x[2]) # sorting with cost    

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
        
        minimumCost = 0
        print("Edges constructed in MST:")
        for u, v, weight in result:
            minimumCost += weight
            print("%d --  %d == %d" % (u, v, w))
        
        print("Minimum cost is", minimumCost)

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

# Assuming you have already defined the Graph class and its methods

# Initialize your graph instance
g = Graph(len(graph))

# Iterate over each key in the graph dictionary
for vertex in graph:
    # Iterate over each adjacent vertex along with its weight
    for adjacent_vertex, weight in graph[vertex].items():
        # Add the edge to the graph
        g.add_edge(vertex, adjacent_vertex, weight)

print(g.kruskalMST())