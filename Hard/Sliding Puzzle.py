# Sliding Puzzle
# O(n), O(n)
def slidingPuzzle(self, board: List[List[int]]) -> int:
    initial_board = tuple(tuple(row) for row in board)
    memo = defaultdict(lambda: math.inf)
    destination = ((1, 2, 3), (4, 5, 0))
    heap = [(0, initial_board)]
    while heap:
        steps, curr_board = heapq.heappop(heap)
        if steps < memo[curr_board]:
            memo[curr_board] = steps
            
            if curr_board == destination:
                break
            zero_index = None
            for row in range(2):
                for col in range(3):
                    if curr_board[row][col] == 0:
                        zero_index = (row, col)
            for d_row, d_col in [(0,1),(1,0),(-1,0),(0,-1)]:
                next_row = zero_index[0] + d_row
                next_col = zero_index[1] + d_col
                if 0 <= next_row < 2 and 0 <= next_col < 3:
                    new_board = [list(row) for row in curr_board]
                    new_board[zero_index[0]][zero_index[1]], new_board[next_row][next_col] = (
                        new_board[next_row][next_col],
                        new_board[zero_index[0]][zero_index[1]],
                    )
                    new_board_tuple = tuple(tuple(row) for row in new_board)
                    heapq.heappush(heap, (steps + 1, new_board_tuple))
            
    if memo[destination] == math.inf:
        return -1
    return memo[destination]