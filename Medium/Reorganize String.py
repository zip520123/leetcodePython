# Reorganize String
# O(n log n), O(n)
def reorganizeString(self, s: str) -> str:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    heap = []
    for key, val in memo.items():
        heapq.heappush(heap, (-val, key))
    res = ""
    while heap:
        curr = heapq.heappop(heap)
        val, key = -curr[0], curr[1]
        if res and res[-1] == key:
            
            if len(heap) == 0:
                return ""
            second_element = heapq.heappop(heap)
            second_val, second_key = -second_element[0], second_element[1]
            res += second_key
            second_val -= 1
            if second_val:
                heapq.heappush(heap, (-second_val, second_key))
            heapq.heappush(heap, (-val, key))
        else:
            res += key
            val -= 1
            if val:
                heapq.heappush(heap, (-val, key))
    return res