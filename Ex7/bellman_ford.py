class Graph:
    def __init__(self, graph = None):
        self.graph = graph
    
    def add_graph(self, graph):
        self.graph = graph
    
    def initialize_parameters(self):
        if len(self.graph) != len(self.graph[0]):
            raise IndexError("Invalid graph!")

        self.num_vertices = len(self.graph)
        
        self.table = {
            i : float("inf") for i in range(len(self.graph))
        }

        self.get_edges()
    
    def get_edges(self):
        edges = []

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] != 0:
                    edges.append((i,j))
        
        self.edges = edges

    def relaxation_step(self, u, v):
        if self.table[u] + self.graph[u][v] < self.table[v]:
            self.table[v] = self.table[u] + self.graph[u][v]
            return True
        return False


    def bellmanFord(self, starting_vertex):
        starting_vertex = starting_vertex - 1
        self.initialize_parameters()
        self.table[starting_vertex] = 0

        for i in range(self.num_vertices):
            for j in range(len(self.edges)):
                self.relaxation_step(self.edges[j][0], self.edges[j][1])
                if i == self.num_vertices - 1:
                    self.shortest_path = self.table.copy()
        
        if self.shortest_path != self.table:
            print("Negative cycle exists in the graph!")
            return None
        
        print("Distance from source:")
        for i in range(self.num_vertices):
            print("{} \t\t {}".format(i+1, self.table[i]))
            
x = [[0,0,0,5],
 [4,0,0,0],
 [0,-10,0,0],
 [0,0,3,0]
]

Graph(x).bellmanFord(4)