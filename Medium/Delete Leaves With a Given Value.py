# Delete Leaves With a Given Value
# O(n), O(n)
def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root == None: return None
    
    root.left = self.removeLeafNodes(root.left, target)
    root.right = self.removeLeafNodes(root.right, target)
    if root.left == None and root.right == None and root.val == target: return None
    return root