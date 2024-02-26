# Design In-Memory File System
# O(n), O(n)
class FileSystem:
    def __init__(self):
        self.root = {}

    def ls(self, path: str) -> List[str]:
        arr = self.pathList(path)
        curr = self.root
        for p in arr:
            curr = curr[p]
        if type(curr) == str:
            return [arr[-1]]
        return sorted(curr.keys())

    def mkdir(self, path: str) -> None:
        arr = self.pathList(path)
        curr = self.root
        for p in arr:
            if p not in curr:
                curr[p] = {}
            curr = curr[p]
        
    def pathList(self, path: str) -> List[str]:
        arr = []
        l, r = 0, 1
        while r < len(path):
            while r < len(path) and path[r] != "/":
                r += 1
            if l+1 < r:
                arr.append(path[l+1:r])
            l = r
            r += 1
        return arr

    def addContentToFile(self, filePath: str, content: str) -> None:
        arr = self.pathList(filePath)
        fileName = arr.pop(-1)
        curr = self.root
        for p in arr:
            curr = curr[p]
        if fileName not in curr:
            curr[fileName] = content
        else:
            curr[fileName] += content

    def readContentFromFile(self, filePath: str) -> str:
        arr = self.pathList(filePath)
        fileName = arr.pop(-1)
        curr = self.root
        for p in arr:
            curr = curr[p]
        if fileName not in curr:
            return ""
        else:
            return curr[fileName]
        

# O(n), O(n) Trie
        
class Trie:
    def __init__(self):
        self.memo = {}
        self.content = None

class FileSystem:

    def __init__(self):
        self.root = Trie()

    def ls(self, path: str) -> List[str]: # O(n log n)
        arr = self.pathList(path)
        curr = self.root
        for p in arr:
            curr = curr.memo[p]
        if curr.content != None:
            return [arr[-1]]
        return sorted(curr.memo.keys())

    def mkdir(self, path: str) -> None: # O(n)
        arr = self.pathList(path)
        curr = self.root
        for p in arr:
            if p not in curr.memo:
                curr.memo[p] = Trie()
            curr = curr.memo[p]
        
    def pathList(self, path: str) -> List[str]:
        arr = []
        l, r = 0, 1
        while r < len(path):
            while r < len(path) and path[r] != "/":
                r += 1
            if l+1 < r:
                arr.append(path[l+1:r])
            l = r
            r += 1
        return arr

    def addContentToFile(self, filePath: str, content: str) -> None: # O(n)
        arr = self.pathList(filePath)
        fileName = arr.pop(-1)
        curr = self.root
        for p in arr:
            curr = curr.memo[p]
        if fileName not in curr.memo:
            curr.memo[fileName] = Trie()
            curr.memo[fileName].content = content
        else:
            curr.memo[fileName].content += content

    def readContentFromFile(self, filePath: str) -> str: # O(n)
        arr = self.pathList(filePath)
        fileName = arr.pop(-1)
        curr = self.root
        for p in arr:
            curr = curr.memo[p]
        if fileName not in curr.memo:
            return ""
        else:
            return curr.memo[fileName].content
