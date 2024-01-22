# Set Mismatch
# O(n), O(n)
def findErrorNums(self, nums: List[int]) -> List[int]:
    res = []
    numsSet = set()
    for n in nums:
        if n in numsSet:
            res.append(n)
        numsSet.add(n)
    for i in range(len(nums)):
        if i+1 not in numsSet:
            res.append(i+1)
    return res