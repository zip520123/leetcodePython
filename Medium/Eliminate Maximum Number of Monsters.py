# Eliminate Maximum Number of Monsters
# O(n log n), O(n), heap
def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
    arr = []
    n = len(dist)
    for i in range(n):
        arr.append(dist[i]/speed[i])
    
    heapq.heapify(arr)

    time = 0
    for i in range(n):
        if arr[0] <= time:
            break
        heapq.heappop(arr)
        time += 1
    return time

# O(n log n), O(n), sort
def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
    arr = []
    n = len(dist)
    for i in range(n):
        arr.append(dist[i]/speed[i])
    
    arr.sort()
    time = 0
    for i in range(n):
        if arr[i] <= time: break
        time += 1
    return time