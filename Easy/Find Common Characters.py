# Find Common Characters
# O(n), O(n)
def commonChars(self, words: List[str]) -> List[str]:
    memo = defaultdict(int)
    for char in words[0]:
        memo[char] += 1
    
    for i in range(1, len(words)):
        word = words[i]
        curr = defaultdict(int)
        for char in word:
            curr[char] += 1
        for key, val in memo.items():
            memo[key] = min(memo[key], curr[key])
    
    res = []
    for key, val in memo.items():
        for _ in range(val):
            res.append(key)

    return res