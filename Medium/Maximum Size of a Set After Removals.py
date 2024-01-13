# Maximum Size of a Set After Removals
# O(n), O(n)
def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
    s1, s2 = set(nums1), set(nums2)
    n1, n2 = len(s1), len(s2)
    c = len(set(s1 & s2))
    n = len(nums1)
    return min(n, min(n//2,n1-c)+min(n//2,n2-c) + c) 