# Meeting Rooms III
# O(n log n), O(n)
def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    heap = []
    meetings.sort()
    for start, end in meetings:
        if heap and start >= heap[0][0]:
            localHeap = []
            while heap and start >= heap[0][0]:
                curr = heapq.heappop(heap)
                heapq.heappush(localHeap, (curr[1], curr[2]))
            curr = heapq.heappop(localHeap)
            heapq.heappush(heap, (end, curr[0], curr[1] + 1 ))
            while localHeap:
                curr = heapq.heappop(localHeap)
                heapq.heappush(heap, (0, curr[0], curr[1]))
        elif len(heap) < n:
            heapq.heappush(heap, (end, len(heap), 1))
        else:
            curr = heapq.heappop(heap)
            d = end-start
            heapq.heappush(heap, (curr[0] + d, curr[1], curr[2] + 1))
    arr = [0] * n
    for end, room, time in heap:
        arr[room] = time
    maxCount = -math.inf
    for time in arr:
        maxCount = max(maxCount, time)
    for i in range(n):
        if arr[i] == maxCount:
            return i
    return 0