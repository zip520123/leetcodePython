# Minimum Cost Path with Edge Reversals
# O(n log n), TLE
def minCost(self, n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    seen = set()
    heap = [(0,0)]
    for node1, node2, weight in edges:
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight * 2))

    
    while heap:
        cost, curr = heapq.heappop(heap)
        if curr == n-1:
            return cost
        for nextNode, weight in graph[curr]:
            if (curr, nextNode, weight) not in seen:
                seen.add((curr, nextNode, weight))
                heapq.heappush(heap, (cost + weight, nextNode))
    return -1

# O(e log v), O(V+E)
def minCost(self, n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    seen = set()
    heap = [(0,0)]
    for node1, node2, weight in edges:
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight * 2))

    dist = [inf] * n

    while heap:
        cost, curr = heapq.heappop(heap)
        if curr == n-1:
            return cost
        if curr in seen:
            continue
        seen.add(curr)
        for nextNode, weight in graph[curr]:
            if dist[nextNode] > cost + weight:
                dist[nextNode] = cost + weight
                heapq.heappush(heap, (cost + weight, nextNode))
    return -1