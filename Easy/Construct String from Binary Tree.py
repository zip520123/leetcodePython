# Construct String from Binary Tree
# O(n), O(h)
def tree2str(self, root: Optional[TreeNode]) -> str:
    res = ""
    if root != None:
        res += str(root.val)
        if root.left != None:
            res += "(" + self.tree2str(root.left) + ")"
        if root.right != None:
            if root.left == None:
                res += "()"
            res += "(" + self.tree2str(root.right) + ")"
    return res