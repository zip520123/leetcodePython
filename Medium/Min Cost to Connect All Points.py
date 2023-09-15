# Min Cost to Connect All Points
# O(n^2), O(n^2)
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    paths = []
    n = len(points)
    for i in range(n-1):
        for j in range(i+1,n):
            p1, p2 = points[i], points[j]
            wei = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
            paths.append((i,j,wei))
    
    paths = sorted(paths, key = lambda x: x[2])
    graph = {}
    for i in range(n):
        graph[i] = i
    
    def find(p: int) -> int:
        if graph[p] != p:
            graph[p] = find(graph[p])
        return graph[p]

    edge, res = 0, 0
    for path in paths:
        p1, p2 = path[0], path[1]
        
        root1, root2 = find(p1), find(p2)
        if root1 != root2:
            res += path[2]
            graph[root1] = root2
            edge += 1
            if edge == n-1:
                break
    return res