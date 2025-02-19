# The k-th Lexicographical String of All Happy Strings of Length n
# O(n*2^n), O(2^n)
def getHappyString(self, n: int, k: int) -> str:
    arr = []

    def backtrack(path) -> bool:
        if len(arr) == k:
            return True
        if len(path) == n:
            arr.append(path)
            return False
        for char in ["a", "b", "c"]:
            if path == "" or char != path[-1]:
                if backtrack(path+char):
                    return True
        return False
    
    backtrack("")

    if len(arr) < k:
        return ""
    return arr[k-1]