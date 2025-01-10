# Word Subsets
# O(words1 * words2), O(words2), TLE
def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    res = []
    for word in words1:
        isSubset = True

        w1 = defaultdict(int)
        for char in word:
            w1[char] += 1
        for w2 in words2:
            w1_copy = dict(w1)
            for char in w2:
                if char not in w1_copy or w1_copy[char] <= 0:
                    isSubset = False
                    break
                w1_copy[char] -= 1

        if isSubset:
            res.append(word)
    return res

# O(words1 + words2), O(words1 + words2)
def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    res = []
    w2 = defaultdict(int)
    for word in words2:
        memo = defaultdict(int)
        for char in word:
            memo[char] += 1
        for key, val in memo.items():
            w2[key] = max(w2[key], val)

    for word in words1:
        isSubset = True

        w1 = defaultdict(int)
        for char in word:
            w1[char] += 1
        for key, val in w2.items():
            if w1[key] < val:
                isSubset = False

        if isSubset:
            res.append(word)
    return res