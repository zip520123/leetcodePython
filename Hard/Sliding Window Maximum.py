# Sliding Window Maximum
# O(n), O(n)
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    queue, res = [], []
    for i,n in enumerate(nums):
        while len(queue) > 0 and nums[queue[-1]] < n:
            queue.pop(-1)
        queue.append(i)
        if i >= k-1:
            res.append(nums[queue[0]])
        if queue[0] == i-k+1:
            queue.pop(0)

    return res