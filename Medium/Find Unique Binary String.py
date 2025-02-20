# Find Unique Binary String
# O(n), O(n)
def findDifferentBinaryString(self, nums: List[str]) -> str:
    n = len(nums)
    maxN = pow(2,n)
    setN = set(nums)
    def toBinary(num: int) -> str:
        res = ""
        num = num
        for i in range(n):
            res = str(num & 1) + res
            num >>= 1
        return res
    for i in range(maxN):
        curr = toBinary(i)
        if curr not in setN:
            return curr
    
    return ""

def findDifferentBinaryString(self, nums: List[str]) -> str:
    n_set = set()
    l = len(nums[0])
    for s in nums:
        num = int(s, 2)
        n_set.add(num)
    for i in range(2 ** 32):
        if i not in n_set:
            return "{0:{fill}{l}b}".format(i, fill="0", l=l)
    return ""