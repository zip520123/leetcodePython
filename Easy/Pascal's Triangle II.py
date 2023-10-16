# Pascal's Triangle II
# O(n), O(n)
def getRow(self, rowIndex: int) -> List[int]:
    arr = []
    for row in range(rowIndex+1):
        curr = []
        for i in range(row+1):
            if i == 0 or i == row:
                curr.append(1)
            else:
                curr.append(arr[row-1][i-1]+arr[row-1][i])
        arr.append(curr)
    return arr[rowIndex]

# O(n), O(1)
def getRow(self, rowIndex: int) -> List[int]:
    arr = []
    for row in range(rowIndex+1):
        curr = []
        for i in range(row+1):
            if i == 0 or i == row:
                curr.append(1)
            else:
                curr.append(arr[i-1]+arr[i])
        arr = curr
    return arr