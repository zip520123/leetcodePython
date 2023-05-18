# Minimum Number of Vertices to Reach All Nodes
# O(n+e) time, O(n) space
def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    hasIncommingNode = [False for _ in range(n)]
    for edge in edges:
        hasIncommingNode[edge[1]] = True
    res = []
    for i in range(n):
        if hasIncommingNode[i] == False:
            res.append(i)
    return res
