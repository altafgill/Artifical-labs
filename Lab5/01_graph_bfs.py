# Graph implementation and Breadth First Search (BFS) using a queue (Task 1).

from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}          # adjacency list: {node: [neighbours]}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # add an undirected edge between two nodes
    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    # breadth first search starting from 'start'
    def bfs(self, start):
        visited = []             # order in which the nodes are visited
        seen = {start}
        queue = deque([start])   # FIFO queue: first in, first out

        while queue:
            node = queue.popleft()
            visited.append(node)

            for neighbour in self.graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)

        return visited


# build the graph given in Task 1
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("The adjacency list of the graph is:")
for node in sorted(g.graph):
    print(" ", node, "->", g.graph[node])

start = int(input("\nEnter the starting node for BFS: "))
print("\nBFS traversal starting from", start, ":", g.bfs(start))
