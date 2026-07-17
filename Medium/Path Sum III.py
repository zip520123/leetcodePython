# Path Sum III
# O(n^2), O(h)
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    if root == None:
        return 0
    
    def dfs(node, curr) -> int:
        if node == None:
            return 0
        res = 0
        if curr - node.val == 0:
            res += 1
        return dfs(node.left, curr - node.val) + dfs(node.right, curr - node.val) + res 
    
    return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

# O(n), O(h)
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

    memo = defaultdict(int)
    memo[0] = 1
    def dfs(node, currSum) -> int:
        nonlocal memo
        if node == None:
            return 0
        currSum+=node.val
        res = memo[currSum-targetSum]
        memo[currSum] += 1
        left = dfs(node.left, currSum)
        right = dfs(node.right, currSum)
        memo[currSum] -= 1
        return res + left + right
    return dfs(root, 0)