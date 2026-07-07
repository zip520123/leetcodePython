# Maximum Score From Removing Stones
# O(nlogn), O(n)
def maximumScore(self, a: int, b: int, c: int) -> int:
    heap = []
    heapq.heappush(heap, -a)
    heapq.heappush(heap, -b)
    heapq.heappush(heap, -c)
    res = 0
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        a -= 1
        b -= 1
        res += 1
        if a > 0:
            heapq.heappush(heap, -a)
        if b > 0:
            heapq.heappush(heap, -b)
    return res

# O(1), O(1)
def maximumScore(self, a: int, b: int, c: int) -> int:
    total = a+b+c
    largest = max(a,b,c)
    return min(total // 2, total - largest)