# Binary Search Tree to Greater Sum Tree
# O(n), O(h)
def bstToGst(self, root: TreeNode) -> TreeNode:
    
    def dfs(node: TreeNode, curr: int) -> int:
        if node == None: return 0
        right = dfs(node.right, curr)
        temp = node.val
        node.val += right + curr
        left = dfs(node.left, node.val)
        return right + temp + left
        
    dfs(root, 0)
    return root