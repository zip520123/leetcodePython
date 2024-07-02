# Intersection of Two Arrays II
# O(n), O(n)
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    memo = defaultdict(int)
    for n in nums1:
        memo[n] += 1
    res = []
    for n in nums2:
        if memo[n] > 0:
            res.append(n)
            memo[n] -= 1
    return res