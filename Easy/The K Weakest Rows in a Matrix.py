# The K Weakest Rows in a Matrix
# O(n log n), O(n)
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    memo = defaultdict(int)
    for i, row in enumerate(mat):
        for col in row:
            if col == 1:
                memo[i] += 1
            else: 
                break
    arr = [i for i in range(len(mat))]
    arr.sort(key = lambda x: memo[x])
    return arr[:k]
