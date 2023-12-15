# Destination City
# O(n), O(n)
def destCity(self, paths: List[List[str]]) -> str:
    graph = defaultdict(lambda: [])
    for path in paths:
        a,b = path[0], path[1]
        graph[a].append(b)
    queue = [paths[0][0]]
    while queue:
        temp = queue
        queue = []
        for node in temp:
            nextNodes = graph[node]
            if len(nextNodes) == 0:
                return node
            for nextNode in nextNodes:
                queue.append(nextNode)
    return ""