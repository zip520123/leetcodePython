# Minimum Number of Removals to Make Mountain Array
# O(n^2), O(n)
def minimumMountainRemovals(self, nums: List[int]) -> int:
    n = len(nums)
    heigher_arr = [0] * n
    lower_arr = [0] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                heigher_arr[i] = max(heigher_arr[i], heigher_arr[j] + 1)
    
    for i in range(n-2, 0, -1):
        for j in range(n-1, i, -1):
            if nums[i] > nums[j]:
                lower_arr[i] = max(lower_arr[i], lower_arr[j] + 1)
    res = math.inf
    for i in range(1, n-1):
        if heigher_arr[i] and lower_arr[i]:
            res = min(res, n-heigher_arr[i]-lower_arr[i]-1)
    
    return res