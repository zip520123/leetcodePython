# Valid Parenthesis String
# O(n^2), O(n)
def checkValidString(self, s: str) -> bool:
    n = len(s)
    @cache
    def dfs(path: str, index: int) -> bool:
        nonlocal n
        if index == n: return len(path) == 0
        char = s[index]
        if char == "(":
            return dfs(path+"(", index+1)
        if char == "*":
            if dfs(path+"(", index+1): return True
            if dfs(path, index+1): return True
            if path and path[-1] == "(":
                if dfs(path[:-1], index+1): return True
        if char == ")":
            if path and path[-1] == "(":
                if dfs(path[:-1], index+1): return True
        return False
    return dfs("", 0)