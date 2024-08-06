# Make Two Arrays Equal by Reversing Subarrays
# O(n), O(n)
def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    memo1 = defaultdict(int)
    memo2 = defaultdict(int)
    for n in target:
        memo1[n] += 1
    for n in arr:
        memo2[n] += 1
    for key, val in memo1.items():
        if key not in memo2 or memo2[key] != val:
            return False
    return True