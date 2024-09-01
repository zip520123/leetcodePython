# Convert 1D Array Into 2D Array
# O(n), O(n)
def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if m*n != len(original):
        return []

    res = []
    curr = []
    for num in original:
        curr.append(num)
        if len(curr) == n:
            res.append(curr)
            curr = []
    return res