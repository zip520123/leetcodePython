# Nested List Weight Sum
# O(n), O(n)
def depthSum(self, nestedList: List[NestedInteger]) -> int:
    def dfs(node: NestedInteger, depth: int) -> int:
        if node.isInteger():
            return node.getInteger() * depth
        res = 0
        for subNode in node.getList():
            res += dfs(subNode, depth+1)
        return res
    return sum([dfs(node, 1) for node in nestedList])

def depthSum(self, nestedList: List[NestedInteger]) -> int:
    def dfs(nodes: List[NestedInteger], depth: int = 1) -> int:
        res = 0
        for node in nodes:
            if node.isInteger():
                res += node.getInteger() * depth
            else:
                res += dfs(node.getList(), depth + 1)
        return res

    return dfs(nestedList)