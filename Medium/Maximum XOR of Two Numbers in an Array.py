# Maximum XOR of Two Numbers in an Array
# O(n*32), O(n), Trie
class Trie:
    def __init__(self):
        self.zero = None
        self.one = None
        self.end = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        for n in nums:
            curr = root
            for i in range(32, -1, -1):
                mask = 2 ** i
                currNum = n & mask
                if currNum == 0:
                    if curr.zero == None:
                        curr.zero = Trie()
                    curr = curr.zero
                else:
                    if curr.one == None:
                        curr.one = Trie()
                    curr = curr.one
            curr.end = n
        res = 0
        for n in nums:
            curr = root
            for i in range(32, -1, -1):
                mask = 2 ** i
                currNum = n & mask
                if currNum == 0:
                    if curr.one != None:
                        curr = curr.one
                    else:
                        curr = curr.zero
                else:
                    if curr.zero != None:
                        curr = curr.zero
                    else:
                        curr = curr.one
            res = max(res, curr.end ^ n)
        return res