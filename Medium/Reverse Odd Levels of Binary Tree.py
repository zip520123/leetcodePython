# Reverse Odd Levels of Binary Tree
# O(n), O(n)
def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None: 
        return root
    queue = [root]
    level = 0
    while queue:
        temp = queue
        queue = []

        for node in temp:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level % 2 == 1:
            l, r = 0, len(temp)-1
            while l<r:
                temp[l].val, temp[r].val = temp[r].val, temp[l].val
                l += 1
                r -= 1
        
        level += 1
    return root