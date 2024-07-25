# Sort Array by Increasing Frequency
# O(n log n), O(n)
def frequencySort(self, nums: List[int]) -> List[int]:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    
    arr = []
    for key, val in memo.items():
        for _ in range(val):
            arr.append((val, -key))
    
    return map(lambda x: -x[1], sorted(arr))

# O(n log n), O(n)
def frequencySort(self, nums: List[int]) -> List[int]:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    
    return sorted(nums, key=lambda n: (memo[n], -n))