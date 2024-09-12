# Count the Number of Consistent Strings
# O(n), O(n)
def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    char_set = set()
    for char in allowed:
        char_set.add(char)
    
    res = 0
    for word in words:

        for char in word:
            if char not in char_set:
                break
        else:
            res += 1
    return res