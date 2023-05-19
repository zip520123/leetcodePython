# Is Graph Bipartite
# O(n+e) time, O(n) space
def isBipartite(self, graph: List[List[int]]) -> bool:
    arr = [-1 for _ in range(len(graph))]
    for i in range(len(graph)):
        if arr[i] == -1:
            arr[i] = 1
        queue = [i]
        while queue:
            node = queue.pop()
            curr = arr[node]
            for next in graph[node]:
                if arr[next] == -1:
                    arr[next] = curr ^ 1
                    queue.append(next)
                else:
                    if arr[next] != curr ^ 1:
                        return False
    return True