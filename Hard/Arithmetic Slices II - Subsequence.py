# Arithmetic Slices II - Subsequence
# O(n^2), O(n)
def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    n = len(nums)
    memo = [defaultdict(int) for _ in range(n)]
    res = 0
    for i in range(1,n):
        for j in range(i):
            diff = nums[i]-nums[j]
            res += memo[j][diff]
            memo[i][diff] += memo[j][diff] + 1
    return res