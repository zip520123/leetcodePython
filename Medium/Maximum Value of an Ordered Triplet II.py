# Maximum Value of an Ordered Triplet II
# O(n), O(n)
def maximumTripletValue(self, nums: List[int]) -> int:
    n = len(nums)
    prefix_max = [num for num in nums]
    suffix_max = [num for num in nums]

    for i in range(1, n): 
        prefix_max[i] = max(prefix_max[i-1], nums[i])
        

    for i in range(n-2,-1, -1):
        suffix_max[i] = max(suffix_max[i+1], nums[i])
    
    res = 0
    for i in range(1, n-1):
        res = max(res, (prefix_max[i-1]-nums[i]) * suffix_max[i+1])
    return res