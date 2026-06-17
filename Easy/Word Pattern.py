# Word Pattern
# O(n), O(n)
def wordPattern(self, pattern: str, s: str) -> bool:
    memo = {}
    arr = s.split(" ")
    used = set()
    if len(pattern) != len(arr):
        return False
    
    for i in range(len(arr)):
        char = pattern[i]
        word = arr[i]
        if char in memo:
            if memo[char] != word:
                return False
        else:
            if word in used:
                return False
            memo[char] = word
            used.add(word)
    return True