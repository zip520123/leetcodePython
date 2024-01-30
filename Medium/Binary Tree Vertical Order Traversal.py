# Binary Tree Vertical Order Traversal
# O(n), O(n), wrong answer
def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    memo = defaultdict(list)
    maxN, minN = 0, 0
    def dfs(index: int, node: Optional[TreeNode]):
        if node == None: return
        nonlocal maxN, minN
        memo[index].append(node.val)
        maxN = max(maxN, index)
        minN = min(minN, index)
        dfs(index-1, node.left)
        dfs(index+1, node.right)
    dfs(0, root)
    res = []
    for n in range(minN, maxN+1):
        res.append(memo[n])
    return res

# O(n), O(n), BFS
def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    memo = defaultdict(list)
    maxN, minN = 0, 0
    if root == None: return []
    queue = [(0, root)]
    while queue:
        temp = queue
        queue = []
        for col, node in temp:
            memo[col].append(node.val)
            maxN = max(maxN, col)
            minN = min(minN, col)
            if node.left != None: 
                queue.append((col-1,node.left))
            if node.right != None:
                queue.append((col+1, node.right))

    res = []
    for n in range(minN, maxN+1):
        res.append(memo[n])
    return res