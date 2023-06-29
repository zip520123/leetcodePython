# Path with Maximum Probability
# O(n log n), O(n)
def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    graph = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, succProb[i]))
        graph[v].append((u, succProb[i]))
    
    arr = [0] * n
    arr[start] = 1
    pq = [(-1, start)]

    while pq:
        prob, node = heapq.heappop(pq)
        if node == end: return -prob
        for (nextNode, nextProb) in graph[node]:
            if -nextProb*prob > arr[nextNode]:
                arr[nextNode] = -nextProb*prob
                heapq.heappush(pq, (nextProb*prob, nextNode))
    return 0