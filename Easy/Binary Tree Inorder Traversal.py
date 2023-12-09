# Binary Tree Inorder Traversal
# O(n), O(h)
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node):
        nonlocal res
        if node != None:
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
    dfs(root)
    return res