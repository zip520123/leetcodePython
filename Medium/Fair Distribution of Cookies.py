# Fair Distribution of Cookies
# O(k^n), O(n+k), TLE without backtrack
def distributeCookies(self, cookies: List[int], k: int) -> int:
    arr = [0] * k
    res = float('inf')
    n = len(cookies)
    def dfs(index: int):
        nonlocal res
        if index == n:
            if min(arr) == 0:
                return
            res = min(res, max(arr))
            return
        for kid in range(k):
            arr[kid] += cookies[index]
            dfs(index+1)
            arr[kid] -= cookies[index]
    dfs(0)
    return res

# O(k^n), O(n+k)
def distributeCookies(self, cookies: List[int], k: int) -> int:
    arr = [0] * k
    res = float('inf')
    n = len(cookies)
    def dfs(index: int):
        nonlocal res
        if index == n:
            res = min(res, max(arr))
            return

        for kid in range(k):
            if n-index-1 < k-kid-1: continue
            arr[kid] += cookies[index]
            dfs(index+1)
            arr[kid] -= cookies[index]
    dfs(0)
    return res

# O(k^n), O(n+k)
def distributeCookies(self, cookies: List[int], k: int) -> int:
    arr = [0] * k
    n = len(cookies)
    
    def dfs(index: int) -> int:
        if index == n:
            return max(arr)

        res = float('inf')
        for kid in range(k):
            if n-index-1 < k-kid-1: continue
            arr[kid] += cookies[index]
            res = min(res, dfs(index+1))
            arr[kid] -= cookies[index]
        return res
    
    return dfs(0)
            