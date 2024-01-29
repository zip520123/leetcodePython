# Palindrome Number
# O(n), O(n)
def isPalindrome(self, x: int) -> bool:
    if x < 0: return False
    s = str(x)
    l, r = 0, len(s)-1
    while l<r:
        if s[l] != s[r]: return False
        l += 1
        r -= 1
    return True

# O(n), O(n)
def isPalindrome(self, x: int) -> bool:
    if x < 0: return False
    arr = []
    curr = x
    while curr:
        arr.append(curr % 10)
        curr //= 10
    arr2 = []
    for n in arr:
        arr2.insert(0, n)
    
    return arr == arr2