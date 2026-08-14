# Lowest Common Ancestor of a Binary Tree
# O(n), O(h)
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    return None