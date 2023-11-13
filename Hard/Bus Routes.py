# Bus Routes
# O(n), O(n)
def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    if source == target: return 0
    graph = defaultdict(lambda: [])
    for i,route in enumerate(routes):
        for stop in route:
            graph[stop].append(i)
    queue = []
    seen = set()
    res = 0
    for routeIndex in graph[source]:
        queue.append(routeIndex)
        seen.add(routeIndex)
    
    while queue:
        temp = queue
        queue = []
        res += 1
        for routeIndex in temp:
            for stop in routes[routeIndex]:
                if stop == target: return res
                for route in graph[stop]:
                    if route not in seen:
                        seen.add(route)
                        queue.append(route)
        
    return -1