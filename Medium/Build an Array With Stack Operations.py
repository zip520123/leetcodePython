# Build an Array With Stack Operations
# O(n), O(n)
def buildArray(self, target: List[int], n: int) -> List[str]:
    res = []
    index = 0
    for curr in range(1,n+1):
        res.append("Push")
        if curr == target[index]:
            index += 1
            if index == len(target): return res
        else:
            res.append("Pop")
    return res