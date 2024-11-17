# Shortest Subarray with Sum at Least K
# O(n log n), O(n)
def shortestSubarray(self, nums: List[int], k: int) -> int:
    heap = []
    n = len(nums)
    pre_sum = 0
    res = math.inf
    for i in range(n):
        pre_sum += nums[i]
        if pre_sum >= k:
            res = min(res, i+1)
        while heap and pre_sum - heap[0][0] >= k:
            pre_val = heapq.heappop(heap)
            res = min(res, i - pre_val[1])
        
        heapq.heappush(heap, (pre_sum, i))
    if res == math.inf:
        return -1
    return res

# O(n), O(n)
def shortestSubarray(self, nums: List[int], k: int) -> int:
    dp = []
    res = math.inf
    pre_sum = 0
    for i in range(len(nums)):
        pre_sum += nums[i]
        if pre_sum >= k:
            res = min(res, i+1)
        while dp and pre_sum - dp[0][0] >= k:
            pre_val, pre_index = dp.pop(0)
            res = min(res, i-pre_index)
        while dp and pre_sum <= dp[-1][0]:
            dp.pop(-1)
        dp.append((pre_sum, i))

    if res == math.inf:
        return -1
    return res

# O(n), O(n), deque
def shortestSubarray(self, nums: List[int], k: int) -> int:
    dp = deque()
    res = math.inf
    pre_sum = 0
    for i in range(len(nums)):
        pre_sum += nums[i]
        if pre_sum >= k:
            res = min(res, i+1)
        while dp and pre_sum - dp[0][0] >= k:
            pre_val, pre_index = dp.popleft()
            res = min(res, i-pre_index)
        while dp and pre_sum <= dp[-1][0]:
            dp.pop()
        dp.append((pre_sum, i))

    if res == math.inf:
        return -1
    return res