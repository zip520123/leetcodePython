# Evaluate Boolean Binary Tree
# O(n), O(n)
def evaluateTree(self, root: Optional[TreeNode]) -> bool:
    if root.left == None and root.right == None:
        if root.val == 0:
            return False
        else:
            return True
    left = self.evaluateTree(root.left)
    right = self.evaluateTree(root.right)
    if root.val == 2: 
        return left or right
    elif root.val ==3:
        return left and right
    return False