# Minimize Maximum Pair Sum in Array
# O(n log n), O(n)
def minPairSum(self, nums: List[int]) -> int:
    n = len(nums)
    arr = sorted(nums)
    res = 0
    for i in range(n//2):
        curr = arr[i] + arr[n-i-1]
        if curr > res: res = curr
    return res