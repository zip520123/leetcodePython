# Kth Smallest Element in a BST
# O(n) time | O(n) space
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root
    steps = 0
    while curr or stack:

        while curr:
            stack.append(curr)
            curr = curr.left
        node = stack.pop(-1)
        steps += 1
        if steps == k:
            return node.val
        curr = node.right
    return 0