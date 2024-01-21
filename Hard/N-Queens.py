# N-Queens
# O(n), O(n)
def solveNQueens(self, n: int) -> List[List[str]]:
    res = []
    mat = [["."]*n for _ in range(n)]
    visited_cols = set()
    visited_diagonals = set()
    visited_antidiagonals = set()

    def dfs(row):
        if row == n:
            res.append(["".join(row) for row in mat])
            return
        for col in range(n):
            diagonal = row - col
            antidiagonal = row + col
            if col not in visited_cols and \
            diagonal not in visited_diagonals and \
            antidiagonal not in visited_antidiagonals:
                visited_cols.add(col)
                visited_diagonals.add(diagonal)
                visited_antidiagonals.add(antidiagonal)
                mat[row][col] = "Q"
                dfs(row+1)
                visited_cols.remove(col)
                visited_diagonals.remove(diagonal)
                visited_antidiagonals.remove(antidiagonal)
                mat[row][col] = "."
    dfs(0)
    return res