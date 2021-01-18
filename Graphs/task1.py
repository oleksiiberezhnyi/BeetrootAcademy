stack = []
used = set()
def dfs(vertex, graph, used):
    # if used is None:
    #     used = set()
    used.add(vertex)
    print(used)
    for next in graph[vertex]:
        if next not in used:
            dfs(next, graph, used)
        else:
            stack.append(next)


graph = {'A': ['B'],
         'B': ['C', 'D'],
         'C': ['A'],
         'D': ['E'],
         'E': ['F'],
         'F': ['D'],
         'G': ['F', 'H'],
         'H': ['I'],
         'I': ['J'],
         'J': ['G'],
         'K': ['J']
         }

print(dfs('A', graph, used))
print(stack)