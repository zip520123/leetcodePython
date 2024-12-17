# Construct String With Repeat Limit
# O(n log n), O(n)
def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    
    heap = []
    for key, val in memo.items():
        heapq.heappush(heap, (-ord(key), key, val))
    
    res = ""

    while heap:
        _, key, count = heapq.heappop(heap)
        if res == "" or res[-1] != key:
            for _ in range(min(count, repeatLimit)):
                res += key
            if count - repeatLimit > 0:
                heapq.heappush(heap, (-ord(key), key, count - repeatLimit))
        elif res and res[-1] == key and heap:
            _, second_key, second_key_count = heapq.heappop(heap)
            heapq.heappush(heap, (-ord(key), key, count))
            
            res += second_key
            if second_key_count - 1 > 0:
                heapq.heappush(heap, (-ord(second_key), second_key, second_key_count - 1))
        else:
            break
    return res