# Even Odd Tree
# O(n), O(n)
def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
    if root == None: return True
    q = [root]
    level = -1
    while q:
        level += 1
        temp = q
        q = []
        for i in range(len(temp)-1):
            if level % 2 == 0: #even level
                if temp[i].val >= temp[i+1].val: return False
            else: #odd level
                if temp[i].val <= temp[i+1].val: return False
        for node in temp:
            if level % 2 == 0: #even level
                if node.val % 2 == 0 : return False
            else: #odd level
                if node.val % 2 != 0: return False
            if node.left != None: q.append(node.left)
            if node.right != None: q.append(node.right)
    return True
