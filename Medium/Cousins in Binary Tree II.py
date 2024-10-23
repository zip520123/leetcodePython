# Cousins in Binary Tree II
# O(n), O(w)
def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    root.val = 0
    queue = [root]
    while queue:
        temp = queue
        queue = []
        all_childs = 0
        for node in temp:
            if node.left:
                all_childs += node.left.val
                queue.append(node.left)

            if node.right:
                all_childs += node.right.val
                queue.append(node.right)
        for node in temp:
            self_child = 0
            if node.left:
                self_child += node.left.val
            if node.right:
                self_child += node.right.val
            if node.left:
                node.left.val = all_childs - self_child
            if node.right:
                node.right.val = all_childs - self_child
    return root