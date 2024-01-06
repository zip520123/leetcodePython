# Minimum Number of Operations to Make Array XOR Equal to K
# O(n), O(n)
def minOperations(self, nums: List[int], k: int) -> int:
    curr = 0
    for n in nums:
        curr = curr ^ n
    curr = curr ^ k
    res = 0
    while curr:
        res += curr & 1
        curr = curr >> 1
    return res