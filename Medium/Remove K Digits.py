# Remove K Digits
# O(n^2), O(n), TLE
def removeKdigits(self, num: str, k: int) -> str:
    if k == len(num): return "0"
    arr = list(num)
    for _ in range(k):
        if arr[0] > arr[1]:
            arr.pop(0)
        else:
            i = 0
            while i+1 < len(arr) and arr[i] <= arr[i+1]:
                i += 1
            arr.pop(i)
    while arr and arr[0] == "0":
        arr.pop(0)
    if not arr:
        return "0"
    return "".join(arr)

# O(n), O(n), stack
def removeKdigits(self, num: str, k: int) -> str:
    stack = []
    for n in num:
        while stack and stack[-1] > n and k > 0:
            stack.pop(-1)
            k -= 1
        stack.append(n)
    while stack and k:
        stack.pop(-1)
        k -= 1
    while stack and stack[0] == "0":
        stack.pop(0)
    if not stack :
        return "0"
    return "".join(stack)