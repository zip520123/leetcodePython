# Plus One
# O(n)
def plusOne(self, digits: List[int]) -> List[int]:
    res = [0] + [n for n in digits]
    n = len(res)
    carry = 1
    
    for i in range(n-1, -1, -1):
        if carry == 1:
            res[i] += 1
        if res[i] == 10:
            res[i] = 0
            carry = 1
        else:
            carry = 0
    if res[0] == 0:
        res.pop(0)
    return res