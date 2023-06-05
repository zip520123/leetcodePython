# Number of Provinces
# O(n), O(n)
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    graph = {}
    n = len(isConnected)
    def find(node: int) -> int:
        if node not in graph:
            graph[node] = node
        if graph[node] != node:
            graph[node] = find(graph[node])
        return graph[node]

    def union(node1: int, node2: int):
        root1 = find(node1); root2 = find(node2)
        graph[root1] = root2
    
    for node1 in range(n):
        for node2 in range(n):
            if isConnected[node1][node2] == 1:
                union(node1, node2)
    
    rootSet = set()
    for node in range(n):
        rootSet.add(find(node))
    return len(rootSet)