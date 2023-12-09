# Largest Odd Number in String
# O(1), O(1)
def largestOddNumber(self, num: str) -> str:
    res = ""
    n = len(num)
    for i in range(n-1,-1,-1):
        if int(num[i]) % 2 == 1:
            res = num[:i+1]
            break
    return res