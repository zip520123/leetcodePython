# Redundant Connection
# O(n), O(n)
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
    graph = {}

    def find(node):
        if node not in graph:
            graph[node] = node
        if graph[node] != node:
            graph[node] = find(graph[node])
        return graph[node]
    
    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        graph[root1] = root2
    
    for a, b in edges:
        root1, root2 = find(a), find(b)
        if root1 == root2:
            return [a,b]
        union(a, b)
    return []