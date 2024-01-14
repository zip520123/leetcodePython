# Determine if Two Strings Are Close
# O(n), O(n)
def closeStrings(self, word1: str, word2: str) -> bool:
    set1, set2 = set(word1), set(word2)
    if set1 != set2: return False

    memo1, memo2 = defaultdict(int), defaultdict(int)
    for char in word1:
        memo1[char] += 1
    for char in word2:
        memo2[char] += 1
    
    memo3, memo4 = defaultdict(int), defaultdict(int)
    for _, val in memo1.items():
        memo3[val] += 1
    for _, val in memo2.items():
        memo4[val] += 1
    return memo3 == memo4