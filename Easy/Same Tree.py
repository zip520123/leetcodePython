# Same Tree
# O(n), O(n)
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p == None and q == None: return True
    if p == None or q == None: return False
    left = self.isSameTree(p.left, q.left)
    right = self.isSameTree(p.right, q.right)
    if left == False: return False
    if right == False: return False
    return p.val == q.val

# O(n), O(n)
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue = [(p,q)]
    while queue:
        temp = queue
        queue = []
        for node1, node2 in temp:
            if node1 == None and node2 == None: continue
            if node1 == None or node2 == None: return False
            if node1.val != node2.val: return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True