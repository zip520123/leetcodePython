# Shifting Letters II
# O(n log n), O(n)
def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    start_heap, end_heap = [], []
    curr = 0
    for start, end, d in shifts:
        direction = 1
        if d == 0:
            direction = -1
        heapq.heappush(start_heap, (start, direction))
        heapq.heappush(end_heap, (end, direction))
    arr = []
    for t in range(len(s)):
        while start_heap and start_heap[0][0] == t:
            start, d = heapq.heappop(start_heap)
            curr += d
        arr.append(curr)
        while end_heap and end_heap[0][0] == t:
            end, d = heapq.heappop(end_heap)
            curr -= d
    res = ""
    for i in range(len(s)):
        shift = arr[i]
        asci = (ord(s[i]) - ord("a") + shift) % 26
        res += chr(asci + ord("a"))
    return res

# O(n), O(n)
def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    arr = [0] * len(s)
    for start, end, d in shifts:
        direction = 1
        if d == 0:
            direction = -1
        arr[start] += direction
        if end + 1 < len(s):
            arr[end+1] -= direction
        
    res = ""
    shift = 0
    for i in range(len(s)):
        shift += arr[i]
        asci = (ord(s[i]) - ord("a") + shift) % 26
        res += chr(asci + ord("a"))
    return res