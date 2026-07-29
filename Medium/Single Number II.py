# Single Number II
# O(n), O(1)
def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for mask in range(32):
        currMask = 2 ** mask
        currOne = 0
        for n in nums:
            if n & currMask:
                currOne += 1
        res += (currOne % 3) * currMask
    if res >= 1 << 31:
        res -= 1 << 32
    return res