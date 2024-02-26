# Cheapest Flights Within K Stops
# O(n^k), O(n), TLE
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for a, b, cost in flights:
        graph[a].append((b, cost))

    heap = [(0,src,0)]
    
    while heap:
        cost, curr, stop = heapq.heappop(heap)
        if curr == dst: return cost
        if stop > k: continue
        for nextNode, nextCost in graph[curr]:
            heapq.heappush(heap, (cost+nextCost, nextNode, stop+1))
    return -1

# O(n log n), O(n)
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for a, b, cost in flights:
        graph[a].append((b, cost))
    stops = [math.inf] * n
    heap = [(0,src,0)]
    
    while heap:
        cost, curr, steps = heapq.heappop(heap)
        if curr == dst: return cost
        if steps > k or stops[curr] < steps: continue
        stops[curr] = steps
        for nextNode, nextCost in graph[curr]:
            heapq.heappush(heap, (cost+nextCost, nextNode, steps+1))
    return -1
