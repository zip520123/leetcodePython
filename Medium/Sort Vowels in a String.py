# Sort Vowels in a String
# O(n log n), O(n)
def sortVowels(self, s: str) -> str:
    vowels = []
    vowelSet = {"a","e","i","o","u","A","E","I","O","U"}
    res = list(s)
    for char in s:
        if char in vowelSet:
            vowels.append(char)
    vowels.sort()
    j = 0
    for i in range(len(s)):
        if res[i] in vowelSet:
            res[i] = vowels[j]
            j += 1
    return "".join(res)