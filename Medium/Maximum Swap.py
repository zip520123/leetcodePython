# Maximum Swap
def maximumSwap(self, num: int) -> int:
    arr = []
    curr = num
    while curr:
        arr.append(curr % 10)
        curr //= 10
    arr.reverse()
    for i in range(len(arr)-1):
        candidate = arr[i]
        candidate_index = i
        for j in range(len(arr)-1, i, -1):
            if candidate < arr[j]:
                candidate = arr[j]
                candidate_index = j
        if candidate_index != i:
            arr[i], arr[candidate_index] = arr[candidate_index], arr[i]
            res = 0
            for k in arr:
                res *= 10
                res += k
            return res
    return num