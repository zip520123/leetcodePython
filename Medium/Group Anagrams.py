# Group Anagrams
# O(n log n * k), O(n)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    memo = defaultdict(list)
    for s in strs:
        curr = defaultdict(int)
        for char in s:
            curr[char] += 1
        memo[tuple(sorted(curr.items()))].append(s)
    res = []
    for val in memo.values():
        res.append(val)
    return res

# O(n * k), O(n)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    memo = defaultdict(list)
    for s in strs:
        curr = [0] * 26
        for char in s:
            curr[ord(char) - ord('a')] += 1
        memo[tuple(curr)].append(s)
    res = []
    for val in memo.values():
        res.append(val)
    return res