# Find Largest Value in Each Tree Row
# O(n), O(w)
def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    if root == None: return []
    res = []
    queue = [root]
    while queue:
        temp = queue
        queue = []
        curr = -float("inf")
        for node in temp:
            curr = max(curr, node.val)
            if node.left != None: queue.append(node.left)
            if node.right != None: queue.append(node.right)
        res.append(curr)
    return res