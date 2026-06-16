# Sum Root to Leaf Numbers
# O(n), O(n)
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node: Optional[TreeNode], path: int = 0):
        nonlocal res
        if node == None: return
        if node.left == None and node.right == None:
            res += path * 10 + node.val
        dfs(node.left, path * 10 + node.val)
        dfs(node.right, path * 10 + node.val)
    dfs(root)
    return res

# O(n), O(n)
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    if root == None: return 0
    res = 0
    queue = [(root, 0)]
    while queue:
        temp = queue
        queue = []
        for node, path in temp:
            if node.left == None and node.right == None:
                res += path*10 + node.val
            if node.left:
                queue.append((node.left, path*10+node.val))
            if node.right:
                queue.append((node.right, path*10+node.val))
    return res

# O(n), O(n)
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(curr: TreeNode, num: int) :
        nonlocal res
        currN = curr.val

        if curr.left:
            dfs(curr.left, num*10 + currN)
        if curr.right:
            dfs(curr.right, num*10 + currN)
        if curr.left == None and curr.right == None:
            res += num*10 + currN
        
    dfs(root, 0)

    return res

# O(n), O(n)
def sumNumbers(self, root: Optional[TreeNode]) -> int:

    def dfs(curr: TreeNode, num: int) -> int:
        res = 0

        if curr.left:
            res += dfs(curr.left, num*10 + curr.val)
        if curr.right:
            res += dfs(curr.right, num*10 + curr.val)
        if curr.left == None and curr.right == None:
            return num*10 + curr.val
        return res

    return dfs(root, 0)