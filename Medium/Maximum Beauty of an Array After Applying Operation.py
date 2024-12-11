# Maximum Beauty of an Array After Applying Operation
# O(n log n), O(n)
def maximumBeauty(self, nums: List[int], k: int) -> int:
    nums.sort()
    res = 0
    queue = []
    for i in range(len(nums)):
        curr = nums[i]
        while queue and nums[queue[0]] + k < curr - k:
            queue.pop(0)
        queue.append(i)
        res = max(res, len(queue))
    return res

# O(n), O(n)
def maximumBeauty(self, nums: List[int], k: int) -> int:
    start_count = defaultdict(int)
    end_count = defaultdict(int)
    max_n = max(nums)
    for n in nums:
        start_count[max(n-k, 0)] += 1
        end_count[min(n+k, max_n)+1] += 1
    curr = 0
    res = 1
    for i in range(max_n):
        curr += start_count[i]
        curr -= end_count[i]
        res = max(res, curr)
    return res