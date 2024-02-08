# Sort Characters By Frequency
# O(n log n), O(n)
def frequencySort(self, s: str) -> str:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    arr = []
    for key, val in memo.items():
        arr.append((val, key))
    arr.sort(key= lambda x: -x[0])
    res = ""
    for val, key in arr:
        for _ in range(val):
            res += key 
    return res