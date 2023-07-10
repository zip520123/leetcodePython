# Minimum Depth of Binary Tree
# O(n), O(h)
def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None: return 0
    if root.left is None or root.right is None:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# O(n), O(w)
def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None: return 0
    level = 0
    queue = [root]
    while queue:
        temp = queue
        queue = []
        level += 1
        for node in temp:
            if node.left is None and node.right is None:
                return level
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return 0
                