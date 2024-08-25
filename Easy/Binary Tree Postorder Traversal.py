# Binary Tree Postorder Traversal
# O(n), O(n)
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root == None: return []
    return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] 