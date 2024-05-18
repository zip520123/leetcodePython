# Distribute Coins in Binary Tree
# O(n), O(n)
def distributeCoins(self, root: Optional[TreeNode]) -> int:
    moves = 0
    def dfs(node):
        if node == None: return 0
        left = dfs(node.left)
        right = dfs(node.right)
        nonlocal moves
        moves += abs(left) + abs(right)
        return node.val - 1 + left + right
    dfs(root)
    return moves