# Find Mode in Binary Search Tree
# O(n), O(n)
def findMode(self, root: Optional[TreeNode]) -> List[int]:
    memo = defaultdict(int)
    def dfs(root: Optional[TreeNode]):
        if root != None:
            memo[root.val] += 1
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    count = 0
    res = []
    for key, val in memo.items():
        if val > count:
            res = [key]
            count = val
        elif val == count:
            res.append(key)
    return res

# O(n), O(1)
def findMode(self, root: Optional[TreeNode]) -> List[int]:
    count, maxCount = 0, -1
    res = []
    prev = None
    def dfs(root: Optional[TreeNode]):
        nonlocal count, maxCount, res, prev
        if root != None:
            dfs(root.left)
            if root.val == prev:
                count += 1
            else:
                count = 1
            if count > maxCount:
                res = [root.val]
                maxCount = count
            elif count == maxCount:
                res.append(root.val)
            prev = root.val
            
            dfs(root.right)
    dfs(root)

    return res