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