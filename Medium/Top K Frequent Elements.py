# Top K Frequent Elements
# O(n log n), O(n) space
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dict = collections.defaultdict(int)
    for n in nums:
        dict[n] += 1
    arr = [key for _,key in enumerate(dict)]
    return sorted(arr, key=lambda key: dict[key], reverse = True)[0:k]

# O(n log k), O(n)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    heap = []
    for key, val in memo.items():
        heapq.heappush(heap, (val, key))
        if len(heap) > k:
            heapq.heappop(heap)
    res = []
    for val, key in heap:
        res.append(key)
    return res

# O(n log n), O(n)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    
    arr = []
    for key, val in memo.items():
        arr.append((-val, key))
    
    arr.sort()

    res = []
    for i in range(k):
        res.append(arr[i][1])
    return res