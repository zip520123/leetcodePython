# Majority Element
# O(n), O(1)
def majorityElement(self, nums: List[int]) -> int:
    res = 0
    count = 0
    for n in nums:
        if n == res:
            count += 1
        else:
            if count == 0:
                res = n
                count = 1
            else:
                count -= 1
    return res