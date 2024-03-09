# Minimum Common Value
# O(n), O(n)
def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    res = math.inf
    set1 = set(nums1)
    for n in nums2:
        if n in set1 and n < res:
            res = n
    if res == math.inf: 
        return -1
    return res