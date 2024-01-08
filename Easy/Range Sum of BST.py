# Range Sum of BST
# O(n), O(h)
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if root == None: return 0
    res = 0
    if low <= root.val <= high:
        res += root.val
    return res + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)