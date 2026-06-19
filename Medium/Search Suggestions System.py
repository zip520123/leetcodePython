# Search Suggestions System
# O(n log n), O(n)
class Trie:
    def __init__(self):
        self.next = defaultdict(Trie)
        self.arr = []
class Solution:
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for p in products:
            curr = root
            for char in p:
                curr = curr.next[char]
                curr.arr.append(p)
        res = []
        curr = root
        for char in searchWord:
            curr = curr.next[char]
            arr = curr.arr.sort()
            res.append(curr.arr[:3])
        
        return res
    
# O(n log n), O(n)
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    res = []
    prefix = ""
    for char in searchWord:
        prefix += char
        idx = bisect_left(products, prefix)
        curr = []
        for i in range(idx, min(len(products), idx + 3)):
            if products[i].startswith(prefix):
                curr.append(products[i])
        res.append(curr)
    return res