# Add One Row to Tree
# O(n), O(n)
def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        node = TreeNode(val, root)
        return node
    def dfs(d: int, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node == None: return None
        if d == depth-1:
            newLeftNode = TreeNode(val, node.left)
            node.left = newLeftNode
            newRightNode = TreeNode(val, None, node.right)
            node.right = newRightNode
            
        else:
            node.left = dfs(d+1, node.left)
            node.right = dfs(d+1, node.right)
        return node
    return dfs(1, root)