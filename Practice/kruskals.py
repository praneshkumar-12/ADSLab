class Graph:
    def __init__(self,  vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, source, destn, cost):
        self.graph.append([source, destn, cost])
    
    def find(self, parent, i):
        # recursive function to find the parent
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        
        return parent[i]
    
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]: # node with higher rank becomes parent
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else: # if ranks are same, first node becomes the parent for the second node
            # rank contains the counter which denotes for how many nodes, the current node is the parent
            parent[y] = x
            rank[x] += 1
    
    def kruskalMST(self):
        result = []

        i = 0 # counter for index (iterating the graph)
        e = 0 # counter for number of edges generated in MST

        self.graph = sorted(self.graph, key = lambda x : x[2]) # sorting with cost 

        parent = [] # initially parent of node is itself
        rank = [] # initially rank of all nodes is 0
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1: # for a graph with n vertices, MST contains n - 1 edges
            source, destn, cost = self.graph[i]
            i += 1

            source_parent = self.find(parent, source)
            destn_parent = self.find(parent, destn)

            if source_parent != destn_parent: 
                # if parents are different, they belong to different sets, so cycle does not form
                # so an edge can be drawn betwewen source and destn
                e += 1
                result.append((source, destn, cost))
                
                # as edge is drawn between source and destination, union should be performed
                # in order to make them into same set
                self.union(parent, rank, source_parent, destn_parent)

        minimum_cost = 0
        print("Edges in  MST:")
        for source, destn, cost in result:
            minimum_cost += cost
            print(f"{source} --> {destn} ==> {cost}")
        
        print("Minimum Cost:", minimum_cost)

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