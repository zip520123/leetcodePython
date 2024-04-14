# Sum of Left Leaves
# O(n), O(h)
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode]) -> int:
        if node == None: return 0
        curr = 0
        if node.left and node.left.left == None and node.left.right == None:
            curr += node.left.val
        else:
            curr += dfs(node.left)
        
        return curr + dfs(node.right)
    return dfs(root)