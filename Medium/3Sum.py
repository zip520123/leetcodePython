# 3Sum
# O(n^2), O(n)
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i+1, len(nums)-1
        while j < k:
            curr = nums[i] + nums[j] + nums[k]
            if curr == 0:
                res.append([nums[i], nums[j], nums[k]])
                while (j+1 < len(nums)-1) and (k-1 >= 0) and nums[j] == nums[j+1] and nums[k] == nums[k-1]:
                    j += 1
                    k -= 1
                j += 1
                k -= 1
            elif curr > 0:
                k -= 1
            else:
                j += 1
    return res
# 
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i+1, len(nums)-1
        while j < k:
            curr = nums[i] + nums[j] + nums[k]
            if curr == 0:
                res.append([nums[i], nums[j], nums[k]])
                while j + 1 < len(nums) and nums[j+1] == nums[j]:
                    j += 1
                while k - 1 >= 0 and nums[k-1] == nums[k]:
                    k -= 1
                j += 1
                k -= 1
            elif curr > 0:
                k -= 1
            else:
                j += 1
    return res