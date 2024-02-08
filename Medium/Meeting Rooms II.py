# Meeting Rooms II
# O(n log n), O(n)
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    startMap = defaultdict(int)
    endMap = defaultdict(int)
    allTime = set()
    for interval in intervals:
        start, end = interval[0], interval[1]
        allTime.add(start)
        allTime.add(end)
        startMap[start] += 1
        endMap[end] += 1
    arr = sorted(list(allTime))
    res = 0
    curr = 0
    
    for t in arr:
        curr += startMap[t]
        curr -= endMap[t]
        res = max(res, curr)
    return res

# O(n log n), O(n)
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    heap = []
    heapq.heapify(heap)

    for interval in sorted(intervals):
        start, end = interval
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)