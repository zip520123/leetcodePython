# Number of Steps to Reduce a Number in Binary Representation to One
# O(n), O(1)
def numSteps(self, s: str) -> int:
    res = 0
    curr = int(s,2)
    while curr != 1:
        res += 1
        if curr & 1 == 0:
            curr >>= 1
        else:
            curr += 1
    return res