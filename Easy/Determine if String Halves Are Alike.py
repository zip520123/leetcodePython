# Determine if String Halves Are Alike
# O(n), O(n)
def halvesAreAlike(self, s: str) -> bool:
    n = len(s)
    a, b = s[:n//2], s[n//2:]
    aCount = 0
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    for char in a:
        if char in vowels:
            aCount += 1
    
    for char in b:
        if char in vowels:
            aCount -= 1
    return aCount == 0