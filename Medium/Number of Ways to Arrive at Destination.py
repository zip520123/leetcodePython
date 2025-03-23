# Number of Ways to Arrive at Destination
# O((n+e)logn) time complexity, O(n+e) space complexity
def countPaths(self, n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(list)
    for start, end, travel_time in roads:
        graph[start].append((end, travel_time))
        graph[end].append((start, travel_time))
    min_travel_time = [math.inf] * n
    ways_to_reach = [0] * n
    ways_to_reach[0] = 1
    priority_queue = [(0, 0)] 
    MOD = (10 ** 9) + 7
    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)
        if current_time > min_travel_time[current_node]:
            continue
        for neighbor, time_to_neighbor in graph[current_node]:
            if current_time + time_to_neighbor < min_travel_time[neighbor]:
                min_travel_time[neighbor] = current_time + time_to_neighbor
                ways_to_reach[neighbor] = ways_to_reach[current_node]
                heapq.heappush(priority_queue, (current_time + time_to_neighbor, neighbor))
            elif current_time + time_to_neighbor == min_travel_time[neighbor]:
                ways_to_reach[neighbor] += ways_to_reach[current_node] % MOD

    return ways_to_reach[n-1] % MOD