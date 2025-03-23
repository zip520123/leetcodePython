# Number of Ways to Arrive at Destination
# O((n+e)logn) time complexity, O(n+e) space complexity
def countPaths(self, n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(list)
    for a, b, t in roads:
        graph[a].append((b,t))
        graph[b].append((a,t))
    shortest_time = [math.inf] * n
    path_count = [0] * n
    path_count[0] = 1
    heap = [(0,0)] 
    MOD = (10 ** 9) + 7
    while heap:
        curr_time, curr_node = heapq.heappop(heap)
        if curr_time > shortest_time[curr_node]:
            continue
        for next_node, road_time in graph[curr_node]:
            if curr_time + road_time < shortest_time[next_node]:
                shortest_time[next_node] = curr_time + road_time
                path_count[next_node] = path_count[curr_node]
                heapq.heappush(heap, (curr_time + road_time, next_node))
            elif curr_time + road_time == shortest_time[next_node]:
                path_count[next_node] += path_count[curr_node] % MOD

    return path_count[n-1] % MOD