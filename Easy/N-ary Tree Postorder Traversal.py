# N-ary Tree Postorder Traversal
# O(n), O(n)
def postorder(self, root: 'Node') -> List[int]:
    if root == None: return []
    res = []
    for node in root.children:
        res += self.postorder(node)
    return  res + [root.val]