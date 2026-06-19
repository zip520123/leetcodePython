# Snakes and Ladders
# djikstra's algorithm, O(n^2 log n), O(n^2)
def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)
    def local(x: int) -> tuple[int, int]:
        # x is 1-indexed
        q, r = divmod(x - 1, n)
        row = n - 1 - q
        if q % 2 == 0:        # left -> right
            col = r
        else:                 # right -> left
            col = n - 1 - r
        return row, col

    heap = [(0,1)] # steps, square
    seen = set()
    seen.add(1)
    while heap:
        curr, square = heapq.heappop(heap)
        if square == n*n:
            return curr
        for i in range(1,7):
            dest = square + i
            if dest > n*n:
                continue
            nextRow, nextCol = local(dest)
            if board[nextRow][nextCol] != -1:
                dest = board[nextRow][nextCol]
            if dest not in seen:
                seen.add(dest)
                heapq.heappush(heap, (curr + 1, dest))
    return -1

# Queue, O(n^2), O(n^2)
def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)
    def local(x: int) -> tuple[int, int]:
        # x is 1-indexed
        q, r = divmod(x - 1, n)
        row = n - 1 - q
        if q % 2 == 0:        # left -> right
            col = r
        else:                 # right -> left
            col = n - 1 - r
        return row, col

    queue = [(0,1)] # steps, square
    seen = set()
    seen.add(1)
    while queue:
        curr, square = queue.pop(0)
        if square == n*n:
            return curr
        for i in range(1,7):
            dest = square + i
            if dest > n*n:
                continue
            nextRow, nextCol = local(dest)
            if board[nextRow][nextCol] != -1:
                dest = board[nextRow][nextCol]
            if dest not in seen:
                seen.add(dest)
                queue.append((curr + 1, dest))
    return -1