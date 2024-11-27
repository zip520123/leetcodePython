# Shortest Distance After Road Addition Queries I
# O(n), O(n)
def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    for i in range(n-1):
        graph[i].append(i+1)
    res = []
    for start, end in queries:
        graph[start].append(end)
        seen = set()
        heap = [(0, 0)]
        seen.add(0)
        while heap:
            steps, node = heapq.heappop(heap)
            if node == n-1:
                res.append(steps)
                break
            for next_node in graph[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    heapq.heappush(heap, (steps+1, next_node))
    return res