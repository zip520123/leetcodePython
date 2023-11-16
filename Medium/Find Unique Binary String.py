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