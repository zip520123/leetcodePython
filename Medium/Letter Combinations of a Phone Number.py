# Letter Combinations of a Phone Number
# O(n!), O(n!)
def letterCombinations(self, digits: str) -> List[str]:
    if digits == "": return []
    map = {
        "2":"abc", 
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }

    res = []

    def dfs(index: int, path: str):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(index, len(digits)):
            char = digits[i]
            if char in map:
                for digit in map[char]:
                    dfs(i+1, path+digit)
    dfs(0,"")
    return res