from collections import defaultdict


class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        self.graph[s].append(d)

    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(f'|{d}|', end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        stack = []
        visited_vertex = [False] * self.V
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        gr = self.transpose()
        visited_vertex = [False] * self.V
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")



g = Graph(11)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 9)
g.add_edge(9, 6)
g.add_edge(10, 9)

print("Strongly Connected Components:")
g.print_scc()
