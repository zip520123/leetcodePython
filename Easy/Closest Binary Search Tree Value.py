# Closest Binary Search Tree Value
# O(n), O(n)
def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    val = math.inf
    diff = math.inf
    def dfs(node: Optional[TreeNode]):
        if node == None: return
        nonlocal val, diff
        dfs(node.left)
        currDiff = abs(target-node.val)
        if currDiff < diff:
            diff = currDiff
            val = node.val
        dfs(node.right)
    dfs(root)
    return val

# O(h), O(1)
def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    if root == None: return 0
    curr = root
    val = root.val
    diff = math.inf
    while curr:
        currDiff = abs(curr.val - target)
        if currDiff == diff:
            val = min(val, curr.val)
        elif currDiff < diff:
            val = curr.val
            diff = currDiff
        curr = curr.left if target < curr.val else curr.right
    return val