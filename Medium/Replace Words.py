# Replace Words
# O(n), O(n)
class Trie:
    def __init__(self):
        self.memo = {}
        self.isEnd = False
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.memo:
                    curr.memo[char] = Trie()
                curr = curr.memo[char]
            curr.isEnd = True

        arr = sentence.split(" ")
        res = []
        for word in arr:
            curr = root
            
            find = False
            for i in range(len(word)):
                char = word[i]
                if char not in curr.memo:
                    break
                curr = curr.memo[char]
                if curr.isEnd:
                    find = True
                    res.append(word[:i+1])
                    break
                    
            if find == False:
                res.append(word)
            
        return " ".join(res)