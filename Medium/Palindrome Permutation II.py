# Palindrome Permutation II
# O((n/2+1)!), O(n)
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        memo = defaultdict(int)
        for char in s:
            memo[char] += 1

        oddChar = None
        for key, val in memo.items():
            if val % 2 == 1:
                if oddChar != None:
                    return []
                oddChar = key
        arr = []
        for key, val in memo.items():
            for _ in range(val//2):
                arr.append(key)
        halfArr = self.permutation(arr)
        res = map(lambda s: self.generate(s, oddChar), halfArr)
        return list(res)

    def permutation(self, arr: List[str]) -> List[str]:
        res = set()
        def dfs(curr: List[str], path: List[str]):
            if len(curr) == 0:
                res.add(tuple(path))
                return
            for i in range(len(curr)):
                dfs(curr[:i] + curr[i+1:], path + [curr[i]])
        dfs(arr, [])
        return res 

    def generate(self, s: List[str], mid: Optional[str]) -> str:
        if mid == None:
            return ''.join(s) + ''.join(reversed(s))
        return ''.join(s) + mid + ''.join(reversed(s))


# O((n/2+1)!), O(n)
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        memo = defaultdict(int)
        for char in s:
            memo[char] += 1

        oddChar = None
        for key, val in memo.items():
            if val % 2 == 1:
                if oddChar != None:
                    return []
                oddChar = key
        arr = []
        for key, val in memo.items():
            for _ in range(val//2):
                arr.append(key)
        halfArr = self.permutation(arr)
        res = map(lambda s: self.generate(s, oddChar), halfArr)
        return list(res)

    def permutation(self, arr: List[str]) -> List[str]:
        res = []
        def dfs(curr: List[str], path: List[str]):
            if len(curr) == 0:
                res.append(path)
                return
            prevChar = None
            for i in range(len(curr)):
                if prevChar == None or prevChar != curr[i]:
                    dfs(curr[:i] + curr[i+1:], path + [curr[i]])
                prevChar = curr[i]
        dfs(arr, [])
        return res 

    def generate(self, s: List[str], mid: Optional[str]) -> str:
        if mid == None:
            return ''.join(s) + ''.join(reversed(s))
        return ''.join(s) + mid + ''.join(reversed(s))
