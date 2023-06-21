# K Radius Subarray Averages
# O(n),O(1)
def getAverages(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = [-1] * n
    if n < 2*k+1: return res
    if k == 0: return nums
    currSum = sum(nums[:2*k+1])
    res[k] = currSum // (2*k+1)

    for i in range(2*k+1,n):
        currSum = currSum - nums[i-(2*k+1)] + nums[i]
        res[i-k] = currSum // (2*k+1)
    return res