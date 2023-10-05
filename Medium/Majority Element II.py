# Majority Element II
# O(n),O(1)
def majorityElement(self, nums: List[int]) -> List[int]:
    v1, v1Count, v2, v2Count = 0,0,1,0
    for n in nums:
        if n == v1:
            v1Count += 1
        elif n == v2:
            v2Count += 1
        elif v1Count == 0:
            v1 = n
            v1Count = 1
        elif v2Count == 0:
            v2 = n
            v2Count = 1
        else:
            v1Count -= 1
            v2Count -= 1
    v1Count = 0
    v2Count = 0
    for n in nums:
        if n == v1: v1Count += 1
        if n == v2: v2Count += 1
    res = []
    if v1Count > len(nums) // 3: res.append(v1)
    if v2Count > len(nums) // 3: res.append(v2)
    return res