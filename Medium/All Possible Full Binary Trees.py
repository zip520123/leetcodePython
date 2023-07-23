# All Possible Full Binary Trees
# O(2^n/2), O(n*2^n/2)
def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    if n % 2 == 0: return []
    if n == 1: return [TreeNode()]
    res = []
    for i in range(1,n):
        leftNodes = self.allPossibleFBT(i)
        rightNodes = self.allPossibleFBT(n-i-1)
        for left in leftNodes:
            for right in rightNodes:
                root = TreeNode()
                root.left = left
                root.right = right
                res.append(root)
    return res

# O(2^n/2), O(n*2^n/2)
def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    if n % 2 == 0: return []

    dp = [[] for _ in range(n+1)]
    dp[1].append(TreeNode())

    for count in range(3, n+1, 2):
        for i in range(1, count-1, 2):
            j = count - 1 - i
            for left in dp[i]:
                for right in dp[j]:
                    root = TreeNode(0, left, right)
                    dp[count].append(root)
    return dp[n]