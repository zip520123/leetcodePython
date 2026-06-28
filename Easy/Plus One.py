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

# O(n), O(1)
def plusOne(self, digits: List[int]) -> List[int]:
    carry = False
    digits[-1] += 1
    for i in range(len(digits)-1, -1, -1):
        if carry:
            digits[i] += 1
            carry = False
        if digits[i] == 10:
            digits[i] = 0
            carry = True
    if carry == True:
        return [1] + digits
    return digits