# Longest Happy String
# O(n log n), O(n)
def longestDiverseString(self, a: int, b: int, c: int) -> str:
    heap = []
    if a: heapq.heappush(heap, (-a, "a"))
    if b: heapq.heappush(heap, (-b, "b"))
    if c: heapq.heappush(heap, (-c, "c"))
    res = []
    while heap:
        count, char = heapq.heappop(heap)
        count = -count
        if len(res) >= 2 and res[-1] == char and res[-2] == char:
            if len(heap) == 0:
                break
            secondCount, secondChar = heapq.heappop(heap)
            secondCount = -secondCount
            secondCount -= 1
            res.append(secondChar)
            if secondCount > 0:
                heapq.heappush(heap, (-secondCount, secondChar))
            heapq.heappush(heap, (-count, char))
        else:
            res.append(char)
            count -= 1
            if count > 0:
                heapq.heappush(heap, (-count, char))
    return "".join(res)