# Interleaving String
# O(s1.len * s2.len), O(s1.len * s2.len)
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    @cache
    def dfs(i: int, j: int, k: int) -> bool:
        if i == len(s1) and j == len(s2) and k == len(s3): return True
            
        res = False
        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            res = res or dfs(i+1,j,k+1)
        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            res = res or dfs(i,j+1,k+1)
        return res
    return dfs(0,0,0)