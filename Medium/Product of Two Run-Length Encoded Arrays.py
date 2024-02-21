# Product of Two Run-Length Encoded Arrays
# O(m+n), O(m+n), MLE
def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
    n = 0
    for _, count in encoded1:
        n += count
    arr1 = [0]*n
    index = 0
    for num, count in encoded1:
        for i in range(index, index+count):
            arr1[i] = num
        index += count
    arr2 = [0]*n
    index = 0
    for num, count in encoded2:
        for i in range(index, index+count):
            arr2[i] = num
        index += count
    products = []
    for i in range(n):
        products.append(arr1[i]*arr2[i])
    res = []
    curr = products[0]
    count = 0
    for i in range(n):
        if products[i] == curr:
            count += 1
        else:
            res.append([curr, count])
            curr = products[i]
            count = 1
    res.append([curr, count])
    return res

# O(m+n), O(1)
def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
    res = []
    i = j = f1 = f2 = a = b = 0 
    while i < len(encoded1) or j < len(encoded2):
        if f1 == 0:
            a, f1 = encoded1[i]
        if f2 == 0:
            b, f2 = encoded2[j]
        currF, p = min(f1, f2), a*b
        if res and res[-1][0] == p:
            res[-1][1] += currF
        else:
            res.append([p, currF])
        f1 -= currF
        f2 -= currF
        if f1 == 0: i += 1
        if f2 == 0: j += 1
    return res