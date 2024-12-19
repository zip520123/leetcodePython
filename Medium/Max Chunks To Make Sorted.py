# Max Chunks To Make Sorted
# O(n), O(n), DP
def maxChunksToSorted(self, arr: List[int]) -> int:
    suffix_min = arr[:]
    prefix_max = arr[:]
    for i in range(1,len(arr)):
        prefix_max[i] = max(prefix_max[i], prefix_max[i-1])
    for i in range(len(arr)-2, -1, -1):
        suffix_min[i] = min(suffix_min[i], suffix_min[i+1])
    chunks = 0
    for i in range(len(arr)):
        if i == 0 or prefix_max[i-1] < suffix_min[i]:
            chunks += 1
    
    return chunks

# O(n), O(1), prefix sum
def maxChunksToSorted(self, arr: List[int]) -> int:
    prefix_sum = 0
    expected_sum = 0
    chunks = 0
    for i in range(len(arr)):
        expected_sum += i
        prefix_sum += arr[i]
        if expected_sum == prefix_sum:
            chunks += 1
    return chunks

# O(n), O(n), Monotonic Increasing Stack
def maxChunksToSorted(self, arr: List[int]) -> int:
    stack = []
    for i in range(len(arr)):
        if stack and stack[-1] > arr[i]:
            curr_max = 0
            while stack and stack[-1] > arr[i]:
                curr_max = max(curr_max, stack.pop(-1))
            stack.append(curr_max)
        else:
            stack.append(arr[i])

    return len(stack)

# O(n), O(1)
def maxChunksToSorted(self, arr: List[int]) -> int:
    max_n = 0
    res = 0
    for i in range(len(arr)):
        max_n = max(max_n, arr[i])
        if max_n == i:
            res += 1
    return res