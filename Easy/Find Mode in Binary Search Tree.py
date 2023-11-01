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
