# Maximum Length of a Concatenated String with Unique Characters
# O(2^n), O(n!)
def maxLength(self, arr: List[str]) -> int:
    dp = [set()]
    for s in arr:
        if len(set(s)) < len(s):
            continue
        curr = set(s)
        for group in dp:
            if curr & group: continue
            dp.append(curr | group)
    return max(map(lambda s: len(s), dp))

def maxLength(self, arr: List[str]) -> int:
    dp = [set()]
    for s in arr:
        curr_set = set(s)
        if len(curr_set) < len(s): continue
        for group in dp:
            if group & curr_set: continue
            dp.append(group | curr_set)
    return max([len(x) for x in dp])

def maxLength(self, arr: List[str]) -> int:
    res = 0
    n = len(arr)
    def dfs(path, index):
        nonlocal res
        res = max(res, len(path))
        if index == n:
            return
        for i in range(index, n):
            curr_set = set(arr[i])
            if len(curr_set) < len(arr[i]): continue
            if path & curr_set: continue
            dfs(path | curr_set, i+1)
            
    dfs(set(), 0)
    return res