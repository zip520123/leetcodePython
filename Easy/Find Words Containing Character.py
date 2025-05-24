# Find Words Containing Character
# O(n), O(1)
def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    res = []
    for i in range(len(words)):
        for char in words[i]:
            if char == x:
                res.append(i)
                break
    return res