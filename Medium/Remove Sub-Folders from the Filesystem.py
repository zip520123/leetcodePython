# Remove Sub-Folders from the Filesystem
# O(n log n), O(n)
class Trie:
    def __init__(self):
        self.memo = {}
        self.isEnd = False
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        folder.sort(key= lambda x: len(x))
        res = []
        for f in folder:
            curr = root
            arr = f[1:].split("/")
            is_sub_folers = False
            for sub in arr:
                if sub not in curr.memo:
                    curr.memo[sub] = Trie()
                curr = curr.memo[sub]
                if curr.isEnd == True:
                    is_sub_folers = True
                    break
                
            curr.isEnd = True
            if is_sub_folers == False:
                res.append(f)

        return res