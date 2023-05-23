# Kth Largest Element in a Stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = sorted(nums)

    def add(self, val: int) -> int:
        l=0;r=len(self.arr)
        while l<r:
            mid = l+((r-l)>>1)
            if self.arr[mid] < val:
                l = mid+1
            else:
                r = mid
        self.arr.insert(l, val)
        return self.arr[len(self.arr)-self.k]
    

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
