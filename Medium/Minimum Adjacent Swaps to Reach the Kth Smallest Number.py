# Minimum Adjacent Swaps to Reach the Kth Smallest Number
# O(nk), O(n)
def getMinSwaps(self, num: str, k: int) -> int:
    n = len(num)
    arr = [char for char in num]
    
    for _ in range(k):
        i = n-2
        while i >= 0:
            if arr[i] < arr[i+1]:
                break
            i -= 1
        j = n-1
        while j >= i:
            if arr[i] < arr[j]:
                break
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        l, r = i+1, n-1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    org = [char for char in num]
    target = "".join(arr)
    res = 0
    for i in range(n):
        if org[i] == target[i]:
            continue
        
        j = i + 1
        while j < n and org[j] != target[i]:
            j += 1
        while j > i:
            org[j], org[j-1] = org[j-1], org[j]
            j -= 1
            res += 1
        
    return res