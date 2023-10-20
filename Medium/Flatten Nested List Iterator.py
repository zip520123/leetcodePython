# Flatten Nested List Iterator
# O(n), O(n)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.index = 0
        def dfs(n: NestedInteger) -> [int]:
            if n.isInteger():
                return [n.getInteger()]
            else:
                arr = []
                for n1 in n.getList():
                    arr += dfs(n1)
                return arr

        self.arr = []
        for arr in map(lambda x: dfs(x), nestedList):
            self.arr += arr
            
    
    def next(self) -> int:
        n = self.arr[self.index]
        self.index += 1
        return n
    
    def hasNext(self) -> bool:
         return self.index < len(self.arr)
    
# O(n), O(n)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.index = 0
        stack = nestedList
        while stack:
            node = stack.pop(0)
            if node.isInteger():
                self.arr.append(node.getInteger())
            else:
                stack = node.getList() + stack
        
    def next(self) -> int:
        n = self.arr[self.index]
        self.index += 1
        return n
    
    def hasNext(self) -> bool:
        return self.index < len(self.arr)