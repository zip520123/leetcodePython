# Word Search II
# O(m*n*4^l), O(l)
class Trie:
    def __init__(self):
        self.isEnd = ""
        self.memo = {}
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        
        for w in words:
            curr = root
            for c in w:
                if c not in curr.memo:
                    curr.memo[c] = Trie()
                curr = curr.memo[c]
            curr.isEnd = w
        rows, cols = len(board), len(board[0])
        res = []
        def dfs(x,y, node):
            if node.isEnd != "":
                res.append(node.isEnd)
                node.isEnd = ""
            
            if not (0 <= x < rows and 0 <= y < cols):
                return 
            if board[x][y] == "." or board[x][y] not in node.memo:
                return
            temp = board[x][y]
            board[x][y] = "."
            child = node.memo[temp]
            dfs(x+1, y, child)
            dfs(x-1, y, child)
            dfs(x, y+1, child)
            dfs(x, y-1, child)
            board[x][y] = temp 
            if len(child.memo) == 0 and child.isEnd == "":
                del node.memo[temp]
        
        for row in range(rows):
            for col in range(cols):
                dfs(row,col, root)
        return res