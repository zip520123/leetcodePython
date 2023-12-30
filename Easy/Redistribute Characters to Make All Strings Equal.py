# Redistribute Characters to Make All Strings Equal
# O(n), O(n)
def makeEqual(self, words: List[str]) -> bool:
    memo = defaultdict(int)
    for word in words:
        for char in word:
            memo[char] += 1
    
    n = len(words)
    for key, val in memo.items():
        if val % n != 0: return False
    return True