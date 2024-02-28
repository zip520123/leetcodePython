# Find Bottom Left Tree Value
# O(n), O(n), BFS
def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    if root == None: return 0
    q = [root]
    res = 0
    while q:
        temp = q
        q = []
        res = temp[0].val
        for node in temp:
            if node.left != None: q.append(node.left)
            if node.right != None: q.append(node.right)
    return res

# O(n), O(n), DFS
def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    if root == None: return 0
    level = 0
    res = root.val
    def dfs(node, currDive):
        if node == None: return
        nonlocal level, res
        if currDive > level:
            level = currDive
            res = node.val
        dfs(node.left, currDive+1)
        dfs(node.right, currDive+1)
    dfs(root, 0)
    return res