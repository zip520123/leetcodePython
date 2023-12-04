# Largest 3-Same-Digit Number in String
# O(n), O(1)
def largestGoodInteger(self, num: str) -> str:
    res = ""
    n = len(num)
    curr = -1
    for i in range(1,n-1):
        if num[i-1] == num[i] == num[i+1]:
            x = int(num[i-1:i+2])
            if x > curr:
                curr = x
                res = num[i-1:i+2]
    return res