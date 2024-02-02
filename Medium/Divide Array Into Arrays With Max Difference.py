# Divide Array Into Arrays With Max Difference
# O(n log n), O(n)
def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i % 3 == 0:
            res.append([])
            res[-1].append(nums[i])
        else:
            if nums[i]-res[-1][-1] > k or (len(res[-1]) == 2 and nums[i]-res[-1][-2] > k): 
                return []
            res[-1].append(nums[i])
    return res