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


class TSP:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.start_node = start_node

        self.visited = {node: False for node in graph}
        self.visited[start_node] = True

        self.min_path = []
        self.min_cost = float("inf")
        self.length = len(self.graph)

    def get_cost(self, path):
        cost = 0

        for idx in range(len(path) - 1):
            cost += self.graph[path[idx]][path[idx + 1]]

        return cost

    def get_visited(self, state):
        return [node for node, status in state.items() if status]

    def get_unvisited(self, state):
        return [node for node, status in state.items() if not status]

    def is_all_visited(self, state):
        return all(state.values())

    def bfs(self):
        queue = [
            (
                [
                    self.start_node,
                ],
                self.visited.copy(),
            )
        ]

        while queue:
            path, visited = queue.pop(0)

            if self.is_all_visited(visited):
                cost = self.get_cost(path + [self.start_node])

                if cost < self.min_cost:
                    self.min_cost = cost
                    self.min_path = path

            for node in self.get_unvisited(visited):
                new_path = path + [node]

                new_state = visited.copy()
                new_state[node] = True

                queue.append((new_path, new_state))

    def dfs(self, copy_dict, path, depth, max_depth=-1):
        if max_depth == -1:
            max_depth = self.length

        if depth == self.length:
            cost = self.get_cost((path + [self.start_node]))

            if cost < self.min_cost:
                self.min_cost = cost
                self.min_path = path[:]
        else:
            for node in self.get_unvisited(copy_dict):
                copy_dict[node] = True
                path.append(node)
                self.dfs(copy_dict, path, depth + 1, max_depth)
                path.pop()
                copy_dict[node] = False

    def iterative_deepening(self):
        max_depth = 1

        copy_dict = self.visited.copy()

        while True:
            self.dfs(
                copy_dict,
                [
                    self.start_node,
                ],
                1,
                max_depth,
            )
            if self.is_all_visited(copy_dict):
                break
            if max_depth >= self.length:
                break
            max_depth += 1


graph1 = {
    "A": {"B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30},
}

t = TSP(graph, "Chicago")

t.bfs()
print(t.min_cost, t.min_path)

t = TSP(graph, "Chicago")

t.dfs(
    t.visited.copy(),
    [
        t.start_node,
    ].copy(),
    1,
)
print(t.min_cost, t.min_path)

t = TSP(graph, "Chicago")
t.iterative_deepening()
print(t.min_cost, t.min_path)
