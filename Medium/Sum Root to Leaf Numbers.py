# Sum Root to Leaf Numbers
# O(n), O(n)
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node: Optional[TreeNode], path: int = 0):
        nonlocal res
        if node == None: return
        if node.left == None and node.right == None:
            res += path * 10 + node.val
        dfs(node.left, path * 10 + node.val)
        dfs(node.right, path * 10 + node.val)
    dfs(root)
    return res