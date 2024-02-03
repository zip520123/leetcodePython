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