# Find if Path Exists in Graph
# O(n), O(n)
def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
    queue = [source]
    seen = set()
    seen.add(source)
    while queue:
        temp = queue
        queue = []
        for node in temp:
            if node == destination:
                return True
            for nextNode in graph[node]:
                if nextNode not in seen:
                    seen.add(nextNode)
                    queue.append(nextNode)
    return False