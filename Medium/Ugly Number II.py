# Ugly Number II
# O(n^2), O(n)
def nthUglyNumber(self, n: int) -> int:
    n_set = set()
    n_set.add(1)
    curr = 1
    for _ in range(n):
        curr = min(n_set)
        n_set.remove(curr)

        n_set.add(curr*2)
        n_set.add(curr*3)
        n_set.add(curr*5)
    return curr

# O(n log n), O(n)
def nthUglyNumber(self, n: int) -> int:
    seen = set()
    seen.add(1)
    heap = [1]
    
    curr = 1
    for _ in range(n):
        curr = heapq.heappop(heap)

        for p in [2,3,5]:
            next_ugly = curr * p
            if next_ugly not in seen:
                heapq.heappush(heap, next_ugly)
                seen.add(next_ugly)
    return curr