# Sum of Digits of String After Convert
# O(n), O(1)
def getLucky(self, s: str, k: int) -> int:
    curr = 0
    for char in s:
        n = ord(char) - ord("a") + 1
        if n < 10:
            curr *= 10
        else:
            curr *= 100
        curr += n
    
    res = 0
    for _ in range(k):
        res = 0
        while curr > 0:
            res += curr % 10
            curr //= 10
        curr = res
        
    return res