# Lexicographically Minimum String After Removing Stars
# O(n log n), O(n)
def clearStars(self, s: str) -> str:
    heap = []
    remove_indeies = set()
    for i in range(len(s)):
        char = s[i]
        if char != "*":
            heapq.heappush(heap, (char, -i))
        else:
            remove_char, remove_index = heapq.heappop(heap)
            remove_indeies.add(-remove_index)
            remove_indeies.add(i)
    res = ""
    for i in range(len(s)):
        if i not in remove_indeies:
            res += s[i]
    return res