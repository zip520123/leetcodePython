# Minimum Operations to Reduce X to Zero
# O(n), O(n)
def minOperations(self, nums: List[int], x: int) -> int:
    res = -float('inf')
    target = sum(nums)-x
    if target == 0: return len(nums)
    map = {0:-1}
    currSum = 0
    for i in range(len(nums)):
        n = nums[i]
        currSum += n
        if currSum-target in map:
            res = max(res, i-map[currSum-target])
        map[currSum] = i

    if res != -float('inf'):
        return len(nums)-res
    
    return -1

# O(n), O(1)
def minOperations(self, nums: List[int], x: int) -> int:
    n = len(nums)
    target = sum(nums)-x
    if target == 0: return len(nums)
    l = r = currSum = 0
    max_len = 0
    while r < n:
        currSum += nums[r]
        while l<=r and currSum > target:
            currSum -= nums[l]
            l += 1
        if currSum == target:
            max_len = max(max_len, r-l+1)
        r += 1
    return n-max_len if max_len else -1