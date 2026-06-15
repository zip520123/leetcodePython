# Game of Life
# O(n), O(1)
def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows, cols = len(board), len(board[0])

    for row in range(rows):
        for col in range(cols):
            
            lives_neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if not (dx == 0 and dy == 0) and (0 <= dx+row < rows) and (0 <= dy+col < cols):
                        if board[dx+row][dy+col] == 1 or board[dx+row][dy+col] == -2 or board[dx+row][dy+col] == -3:
                            lives_neighbors += 1
            if board[row][col] == 0:
                if lives_neighbors == 3:
                    board[row][col] = -1
            else:
                if lives_neighbors < 2:
                    board[row][col] = -2
                elif lives_neighbors == 2 or lives_neighbors == 3:
                    board[row][col] = -3
                elif lives_neighbors > 3:
                    board[row][col] = -2
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == -1:
                board[row][col] = 1
            elif board[row][col] == -2:
                board[row][col] = 0
            elif board[row][col] == -3:
                board[row][col] = 1
            elif board[row][col] == -4:
                board[row][col] = 0