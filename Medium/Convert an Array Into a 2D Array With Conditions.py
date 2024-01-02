# Convert an Array Into a 2D Array With Conditions
# O(n), O(n)
def findMatrix(self, nums: List[int]) -> List[List[int]]:
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
    
    res = []
    for key, val in memo.items():
        for row in range(val):
            if len(res) == row:
                res.append([])
            res[row].append(key)
    return res