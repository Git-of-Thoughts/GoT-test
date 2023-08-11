from collections import deque
from graph import Graph

def breadth_first_search(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            neighbours = graph.graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)

    return visited
