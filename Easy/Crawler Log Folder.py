# Crawler Log Folder
# O(n), O(1)
def minOperations(self, logs: List[str]) -> int:
    deep = 0
    for op in logs:
        if op == "../":
            if deep > 0: deep -= 1
        elif op == "./":
            pass
        else:
            deep += 1
    return deep