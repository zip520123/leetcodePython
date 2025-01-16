# Bitwise XOR of All Pairings
# O(n+m), O(1)
def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
    n1, n2 = len(nums1), len(nums2)
    xor_1 = 0
    if n2 % 2 == 1:
        for n in nums1:
            xor_1 ^= n
    xor_2 = 0
    if n1 % 2 == 1:
        for n in nums2:
            xor_2 ^= n
    return xor_1 ^ xor_2