# Minimum Absolute Difference in BST
# O(n), O(n)
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    res = float('inf')
    prev = None
    def dfs(node: Optional[TreeNode]):
        nonlocal res, prev
        if node == None: return
        dfs(node.left)
        if prev != None:
            res = min(res, abs(node.val-prev.val))
        prev = node
        dfs(node.right)
    
    dfs(root)
    return res

# O(n), O(n)
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    if root == None : return 0
    stack = []
    res = float('inf')
    curr = root
    prev = None
    while curr != None or stack:
        while curr != None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop(-1)
        if prev != None:
            res = min(res, abs(prev.val-curr.val))
        prev = curr
        curr = curr.right
    
    return res