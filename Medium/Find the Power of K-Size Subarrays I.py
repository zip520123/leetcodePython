# Find the Power of K-Size Subarrays I
# O(n), O(n)
def resultsArray(self, nums: List[int], k: int) -> List[int]:
    res = []
    stack = []
    for i in range(len(nums)):
        if stack and stack[-1] != nums[i] -1:
            stack = []
        stack.append(nums[i])

        if i-k+1>=0:
            if len(stack) == k:
                res.append(stack[-1])
                stack.pop(0)
            else:
                res.append(-1)
    return res