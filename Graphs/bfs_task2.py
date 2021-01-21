from collections import defaultdict


edges = [
    ["Kyiv", "Chernihiv"], ["Chernihiv", "Sumy"],
    ["Kyiv", "Poltava"], ["Poltava", "Sumy"],
    ["Poltava", "Kharkiv"], ["Sumy", "Kharkiv"],
    ["Poltava", "Dnipro"], ["Kharkiv", "Dnipro"],
    ["Dnipro", "Donetsk"], ["Kharkiv", "Donetsk"]
    ]


def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs_sp(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        print("Same Node")
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
    print("So sorry, but a connecting path doesn't exist")
    return


graph = build_graph(edges)
print(graph)
bfs_sp(graph, 'Chernihiv', 'Donetsk')

