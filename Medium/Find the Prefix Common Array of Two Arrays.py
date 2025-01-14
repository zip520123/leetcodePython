# Find the Prefix Common Array of Two Arrays
# O(n), O(n)
def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    a_set, b_set = set(), set()
    res = [0] * len(A)
    common = 0
    for i in range(len(A)):
        curr_a, curr_b = A[i], B[i]
        if curr_a in b_set:
            common += 1
        a_set.add(curr_a)
        if curr_b in a_set:
            common += 1
        b_set.add(curr_b)
        res[i] = common
    return res