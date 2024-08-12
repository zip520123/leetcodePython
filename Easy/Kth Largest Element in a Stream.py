# Kth Largest Element in a Stream
# O(n^2), O(n)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        l, r = 0, len(self.arr)
        
        while l<r:
            mid = l+((r-l)>>1)
            if self.arr[mid] < val:
                l = mid+1
            else:
                r = mid

        self.arr.insert(l, val)
        return self.arr[len(self.arr)-self.k]
    
# O(n log n), O(n)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for n in nums:
            self.add(n)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]