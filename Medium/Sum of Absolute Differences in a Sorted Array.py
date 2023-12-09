# Sum of Absolute Differences in a Sorted Array
# O(n), O(1)
def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    res = []
    n = len(nums)
    rsum, lsum = sum(nums), 0
    for i in range(n):
        curr = nums[i]
        res.append( rsum - curr * (n - i) + curr * i - lsum)
        rsum -= curr
        lsum += curr
    return res