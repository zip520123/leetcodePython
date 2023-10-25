#  K-th Symbol in Grammar
# O(n), O(n)
def kthGrammar(self, n: int, k: int) -> int:
    def dfs(n,k,root) -> int:
        if n == 1: return root
        totalNodes = pow(2, n-1)
        if k > totalNodes // 2:
            nextRoot = 1 if root == 0 else 0
            return dfs(n-1, k-totalNodes//2 , nextRoot)
        else:
            nextRoot = 0 if root == 0 else 1
            return dfs(n-1, k, nextRoot)

    return dfs(n,k,0)