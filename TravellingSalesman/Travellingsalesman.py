import matplotlib.pyplot as plt
import networkx as nx


class TSP:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start

    def actions(self, state):
        return [city for city in self.graph[state] if city != self.start]

    def goal_test(self, state):
        return set(state) == set(self.graph.keys())

    def path_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph[path[i]][path[i + 1]]
        cost += self.graph[path[-1]][self.start]  # return to start
        return cost


def dfs(problem, state, visited=None):
    if visited is None:
        visited = set()
    visited.add(state)
    if problem.goal_test(visited):
        return list(visited) + [problem.start]
    for action in problem.actions(state):
        if action not in visited:
            result = dfs(problem, action, visited.copy())
            if result is not None:
                return result


def bfs(problem):
    queue = [[problem.start]]
    while queue:
        path = queue.pop(0)
        state = path[-1]
        if problem.goal_test(path):
            return path
        for action in problem.actions(state):
            new_path = list(path)
            new_path.append(action)
            queue.append(new_path)


def iterative_deepening(problem):
    depth = 1
    while True:
        result = depth_limited_dfs(problem, problem.start, depth)
        if result is not None:
            return result
        depth += 1


def depth_limited_dfs(problem, state, depth, visited=None):
    if visited is None:
        visited = set()
    visited.add(state)
    if problem.goal_test(visited):
        return list(visited) + [problem.start]
    if depth == 0:
        return None
    for action in problem.actions(state):
        if action not in visited:
            result = depth_limited_dfs(problem, action, depth - 1, visited.copy())
            if result is not None:
                return result


def visualize_graph_with_path(graph, optimal_path):
    G = nx.Graph()

    # Add nodes
    for city in graph.keys():
        G.add_node(city)

    # Add edges
    for city, connections in graph.items():
        for neighbor, distance in connections.items():
            G.add_edge(city, neighbor, weight=distance)

    # Draw graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10)

    # Draw optimal path
    optimal_edges = [
        (optimal_path[i], optimal_path[i + 1]) for i in range(len(optimal_path) - 1)
    ]
    nx.draw_networkx_edges(G, pos, edgelist=optimal_edges, width=2, edge_color="red")

    # Label edges with weights
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Graph with Optimal Path")
    plt.show()


if __name__ == "__main__":
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

    start = "New York"

    problem = TSP(graph, start)

    # DFS
    print("DFS:", dfs(problem, start))

    # BFS
    print("BFS:", bfs(problem))

    # Iterative Deepening
    print("Iterative Deepening:", iterative_deepening(problem))

    optimal_path = iterative_deepening(
        problem
    )  # Use any of the search algorithms to find the optimal path
    visualize_graph_with_path(graph, optimal_path)
