class Graph:
    def __init__(self, graph=None):
        # Initialize the graph
        self.graph = graph
    
    def add_graph(self, graph):
        # Method to add a graph
        self.graph = graph
    
    def initialize_parameters(self):
        # Initialize parameters for Bellman-Ford algorithm
        if len(self.graph) != len(self.graph[0]):
            raise IndexError("Invalid graph!")  # Ensure square matrix

        self.num_vertices = len(self.graph)  # Number of vertices
        
        # Initialize distance table with infinity
        self.table = {
            i: float("inf") for i in range(len(self.graph))
        }

        self.get_edges()  # Get edges from the graph
    
    def get_edges(self):
        # Get edges from the graph
        edges = []

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] != 0:
                    edges.append((i, j))  # Store non-zero edges
        
        self.edges = edges  # Store the edges
    
    def relaxation_step(self, u, v):
        # Relaxation step of the Bellman-Ford algorithm
        if self.table[u] + self.graph[u][v] < self.table[v]:
            self.table[v] = self.table[u] + self.graph[u][v]
            return True  # Update distance if shorter path is found
        return False  # No update needed
    
    def bellmanFord(self, starting_vertex):
        starting_vertex = starting_vertex - 1  # Adjust for 0-based indexing
        self.initialize_parameters()  # Initialize parameters
        self.table[starting_vertex] = 0  # Set distance to starting vertex as 0

        # Run relaxation step |V| - 1 times
        for i in range(self.num_vertices):
            for j in range(len(self.edges)):
                self.relaxation_step(self.edges[j][0], self.edges[j][1])
                if i == self.num_vertices - 1:
                    self.shortest_path = self.table.copy()  # Store shortest path
        
        # Check for negative cycles
        if self.shortest_path != self.table:
            print("Negative cycle exists in the graph!")
            return None
        
        # Print distances from source
        print("Distance from source:")
        for i in range(self.num_vertices):
            print("{} \t\t {}".format(i+1, self.table[i]))
            
# Example usage
x = [[0, 0, 0, 5],
     [4, 0, 0, 0],
     [0, -10, 0, 0],
     [0, 0, 3, 0]
]

Graph(x).bellmanFord(4)
