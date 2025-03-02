# Merge Two 2D Arrays by Summing Values
# O(n), O(1)
def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    res = []
    l, r = 0, 0
    while l < len(nums1) and r < len(nums2):
        curr = None
        if nums1[l][0] < nums2[r][0]:
            curr = nums1[l]
            l += 1
        else:
            curr = nums2[r]
            r += 1
        if res and res[-1][0] == curr[0]:
            res[-1][1] += curr[1]
        else:
            res.append(curr)
    while l<len(nums1):
        curr = nums1[l]
        if res and res[-1][0] == curr[0]:
            res[-1][1] += curr[1]
        else:
            res.append(curr)
        l += 1
    while r<len(nums2):
        curr = nums2[r]
        if res and res[-1][0] == curr[0]:
            res[-1][1] += curr[1]
        else:
            res.append(curr)
        r += 1
    return res