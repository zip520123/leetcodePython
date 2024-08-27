# Path with Maximum Probability
# O(e log n), O(n)
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

# O(e log n), O(n)
def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    graph = defaultdict(list)
    
    for i in range(len(edges)):
        node1, node2 = edges[i][0], edges[i][1]
        p = succProb[i]
        graph[node1].append((node2, p))
        graph[node2].append((node1, p)) 

    heap = [(-1, start_node)]

    arr = [0] * n
    arr[start_node] = 1
    while heap:
        p, node = heapq.heappop(heap)
        p = -p
        if node == end_node: return p
        
        for next_node, next_probability in graph[node]:
            if arr[next_node] < p * next_probability:
                arr[next_node] = p * next_probability 
                heapq.heappush(heap, (-p * next_probability, next_node))
    return 0