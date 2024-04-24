# Minimum Height Trees
# O(n^2), O(n) TLE
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    res = []
    steps = math.inf
    for node in range(n):
        currSteps = 0
        seen = set()
        seen.add(node)
        queue = [node]
        while queue:
            temp = queue
            queue = []
            for curr in temp:
                for nextNode in graph[curr]:
                    if nextNode not in seen:
                        seen.add(nextNode)
                        queue.append(nextNode)
            currSteps += 1
            if len(queue) == 0:
                if currSteps < steps:
                    steps = currSteps
                    res = [node]
                elif currSteps == steps:
                    res.append(node)
    return res

# O(n), O(n)
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n < 2: return [i for i in range(n)]
    
    graph = defaultdict(list)
    degree = [0] * n
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
        degree[node1] += 1
        degree[node2] += 1

    leaves = [i for i in range(n) if degree[i] == 1]

    remaining_nodes = n
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        temp = leaves
        leaves = []
        for node in temp:
            for nei in graph[node]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    leaves.append(nei)
    return leaves