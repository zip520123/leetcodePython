# Restore the Array From Adjacent Pairs
# O(n), O(n), BFS
def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    graph = defaultdict(lambda: [])
    for pair in adjacentPairs:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    root = 0
    for key, val in graph.items():
        if len(val) == 1:
            root = key
            break
    queue = [root]
    seen = set()
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node)
        seen.add(node)
        for next in graph[node]:
            if next not in seen:
                queue.append(next)
    return res

# O(n), O(n), DFS
def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    graph = defaultdict(lambda: [])
    for pair in adjacentPairs:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    root = 0
    for key, val in graph.items():
        if len(val) == 1:
            root = key
            break
    
    res = []
    def dfs(prev, node):
        res.append(node)
        for next in graph[node]:
            if next != prev:
                dfs(node,next)
    dfs(None, root)
    return res