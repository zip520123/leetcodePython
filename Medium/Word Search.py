# Word Search
# O(board*word), O(n)
def exist(self, board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(x: int, y: int, index: int) -> bool:
        if index == len(word): return True
        if not (0 <= x < rows and 0 <= y < cols): return False
        nonlocal board
        if board[x][y] == "." or board[x][y] != word[index]: return False
        board[x][y] = "."
        res = False
        res |= dfs(x+1,y,index+1)
        res |= dfs(x-1,y,index+1)
        res |= dfs(x,y+1,index+1)
        res |= dfs(x,y-1,index+1)
        board[x][y] = word[index]
        return res
        
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False

# O(board*word), O(n)
def exist(self, board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    def dfs(i, x, y) -> bool:
        if i == len(word):
            return True
        if not (0 <= x < rows and 0 <= y < cols and word[i] == board[x][y]):
            return False
        if board[x][y] == -1:
            return False
        temp = board[x][y]
        board[x][y] = -1
        curr = False
        curr = curr | dfs(i+1, x+1, y)
        curr = curr | dfs(i+1, x-1, y)
        curr = curr | dfs(i+1, x, y+1)
        curr = curr | dfs(i+1, x, y-1)
        board[x][y] = temp
        return curr
    for row in range(rows):
        for col in range(cols):
            if dfs(0, row, col):
                return True
    return False
        