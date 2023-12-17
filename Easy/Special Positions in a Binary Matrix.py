# Special Positions in a Binary Matrix
# O(n), O(1)
def numSpecial(self, mat: List[List[int]]) -> int:
    res = 0
    rows, cols = len(mat), len(mat[0])
    for row in range(rows):
        if sum(mat[row]) == 1:
            for col in range(cols):
                if mat[row][col] == 1:
                    curr = 0
                    for i in range(rows):
                        if mat[i][col] == 1:
                            curr += 1
                    if curr == 1:
                        res += 1
    return res