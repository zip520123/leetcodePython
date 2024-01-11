# Range Sum of BST
# O(n), O(h)
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if root == None: return 0
    res = 0
    if low <= root.val <= high:
        res += root.val
    return res + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# O(n), O(w)
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if root == None: return 0
    q = [root]
    res = 0
    while q:
        temp = q
        q = []
        for node in temp:
            if low <= node.val <= high:
                res += node.val
            if node.left != None: q.append(node.left)
            if node.right != None: q.append(node.right)
    return res