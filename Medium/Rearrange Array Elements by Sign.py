# Rearrange Array Elements by Sign
# O(n), O(n)
def rearrangeArray(self, nums: List[int]) -> List[int]:
    q1, q2 = [], []
    for n in nums:
        if n > 0:
            q1.append(n)
        if n < 0:
            q2.append(n)
    res = []
    i, j = 0, 0
    while i<len(q1) and j<len(q2):
        res.append(q1[i])
        res.append(q2[j])
        i += 1
        j += 1
    return res