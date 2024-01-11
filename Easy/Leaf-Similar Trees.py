# Leaf-Similar Trees
# O(n), O(h)
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode]) -> [int]:
        if node == None: return []
        if node.left == None and node.right == None: return [node.val]
        return dfs(node.left) + dfs(node.right)
    return dfs(root1) == dfs(root2)

# O(n), O(w)
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def bfs(node: Optional[TreeNode]) -> [int]:
        stack = []
        curr = node
        res = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop(-1)
            if curr.left == None and curr.right == None:
                res.append(curr.val)
            curr = curr.right
        return res
        
    return bfs(root1) == bfs(root2)