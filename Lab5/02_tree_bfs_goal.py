# tree implementation and Breadth First Search (BFS) using a queue (Task 2)
# start node = A, goal node = G, the search stops as soon as the goal is reached


class Queue:
    def __init__(self):
        self.queue = []

    # enqueue
    def enqueue(self, x):
        self.queue.append(x)

    # dequeue
    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


class Tree:
    def __init__(self):
        self.tree = {}           # adjacency list {node : [children]}

    def add_node(self, node):
        if node not in self.tree:
            self.tree[node] = []

    # a tree edge goes from parent to child
    def add_edge(self, parent, child):
        self.add_node(parent)
        self.add_node(child)
        self.tree[parent].append(child)

    # BFS from 'start' that stops when 'goal' is dequeued
    def bfs_goal(self, start, goal):
        parent = {start: None}   # used to rebuild the path
        visited = []
        q = Queue()
        q.enqueue(start)

        while not q.is_empty():
            node = q.dequeue()
            visited.append(node)

            if node == goal:
                # rebuild the path from start to goal
                path = []
                current = goal
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return visited, path

            for child in self.tree[node]:
                if child not in parent:
                    parent[child] = node
                    q.enqueue(child)

        return visited, []       # goal not found


# building the tree given in Task 2 (A is the root and G is the goal)
t = Tree()
t.add_edge('A', 'B')
t.add_edge('A', 'F')
t.add_edge('A', 'D')
t.add_edge('A', 'E')
t.add_edge('B', 'K')
t.add_edge('B', 'J')
t.add_edge('K', 'N')
t.add_edge('K', 'M')
t.add_edge('D', 'G')
t.add_edge('E', 'C')
t.add_edge('E', 'H')
t.add_edge('E', 'I')
t.add_edge('I', 'L')

print("The adjacency list of the tree is :")
for node in t.tree:
    print(" ", node, "->", t.tree[node])

visited, path = t.bfs_goal('A', 'G')
print("\nBFS order (stopped when goal G was reached) :", visited)
print("Path from A to G :", " -> ".join(path))
