# Maximum Average Pass Ratio
# O(n log n), O(n)
def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    heap = []
    for p, total in classes:
        change = p/total - (p+1) / (total+1)
        heapq.heappush(heap, (change, p, total))
    
    for _ in range(extraStudents):
        _ , p, total = heapq.heappop(heap)
        next_change = (p+1)/(total+1) - (p+2) / (total+2)
        heapq.heappush(heap, (next_change, p + 1, total + 1))
    
    res = 0
    for ratio, p , total in heap:
        res += (p / total)
    return res / len(heap)