# The Knight’s Tour
# O(8^(m*n)), O(m*n)
def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
    moves = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2)
    ]

    board = [[0] * n for _ in range(m)]
    board[r][c] = -1

    def backtrack(x,y,move_count) -> bool:
        if move_count == m*n:
            return True
        nonlocal board
        for dx, dy in moves:
            nextX, nextY = x+dx, y+dy
            if 0 <= nextX < m and 0 <= nextY < n and board[nextX][nextY] == 0:
                board[nextX][nextY] = move_count
                if backtrack(x+dx, y+dy, move_count + 1):
                    return True
                board[nextX][nextY] = 0
        return False
    backtrack(r,c,1)
    board[r][c] = 0
    return board