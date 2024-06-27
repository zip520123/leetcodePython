# Find Center of Star Graph
# O(1), O(1)
def findCenter(self, edges: List[List[int]]) -> int:
    nodes = set()
    nodes.add(edges[0][0])
    nodes.add(edges[0][1])
    if edges[1][0] in nodes:
        return edges[1][0]
    if edges[1][1] in nodes:
        return edges[1][1]
    return 0