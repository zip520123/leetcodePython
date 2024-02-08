# Group Shifted Strings
# O(n), O(n)
def groupStrings(self, strings: List[str]) -> List[List[str]]:
    memo = defaultdict(list)
    for s in strings:
        arr = []
        for i in range(len(s)-1):
            arr.append((ord(s[i]) - ord(s[i+1]) + 26) % 26)
        memo[tuple(arr)].append(s)
    return memo.values()