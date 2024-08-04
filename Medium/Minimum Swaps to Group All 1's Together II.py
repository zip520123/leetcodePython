# Minimum Swaps to Group All 1's Together II
# O(n), O(n)
def minSwaps(self, nums: List[int]) -> int:
    n = len(nums)
    l, r = 0, n-1
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
    if ones == 0: return 0
    res = math.inf
    arr = nums + nums
    curr_zero = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            curr_zero += 1
        if i-ones+1 >= 0 :
            res = min(res, curr_zero)
            if arr[i-ones+1] == 0:
                curr_zero -= 1
    if res == math.inf: return 0
    return res