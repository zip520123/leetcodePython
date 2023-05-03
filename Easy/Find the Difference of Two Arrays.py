#Find the Difference of Two Arrays
#O(n), O(n)
def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = set(nums1)
    res2 = set()
    for n in nums2:
        if (n in set1) == False:
            res2.add(n)
    set2 = set(nums2)
    res1 = set()
    for n in nums1:
        if (n in set2) == False:
            res1.add(n)
    return [res1,res2]