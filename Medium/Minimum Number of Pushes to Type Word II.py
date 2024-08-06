# Minimum Number of Pushes to Type Word II
# O(n log n), O(n)
def minimumPushes(self, word: str) -> int:
    memo = defaultdict(int)
    for char in word:
        memo[char] += 1
    arr = []
    for key, val in memo.items():
        arr.append((val, key))
    arr.sort(reverse = True)
    res = 0
    for i in range(len(arr)):
        count, _ = arr[i]
        res += count * ((i // 8) + 1)
    return res

# O(n), O(1)
def minimumPushes(self, word: str) -> int:
    freq = [0] * 26
    for char in word:
        freq[ord(char)-ord("a")] += 1
    freq.sort(reverse=True)
    res = 0
    for i in range(26):
        res += freq[i] * ((i // 8) + 1)
    return res