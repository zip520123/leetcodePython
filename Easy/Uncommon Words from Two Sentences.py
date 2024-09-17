# Uncommon Words from Two Sentences
# O(n), O(n)
def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    words1, words2 = s1.split(" "), s2.split(" ")
    words1_memo = defaultdict(int)
    for word in words1:
        words1_memo[word] += 1
    res = []
    words2_memo = defaultdict(int)
    for word in words2:
        words2_memo[word] += 1

    for word in words2:
        if word not in words1_memo and words2_memo[word] == 1:
            res.append(word)
    
    for word in words1:
        if word not in words2_memo and words1_memo[word] == 1:
            res.append(word)
    return res