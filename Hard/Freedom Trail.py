# Freedom Trail
# O(n log n), O(ring*key)
def findRotateSteps(self, ring: str, key: str) -> int:
    dp = [[math.inf] * len(key) for _ in range(len(ring))]
    heap = [(0,0,0)]
    while heap:
        steps, ring_index, key_index = heapq.heappop(heap)
        if ring[ring_index] == key[key_index]:
            key_index += 1
            steps += 1
            if key_index == len(key): 
                return steps
            heapq.heappush(heap, (steps, ring_index, key_index))
        if steps >= dp[ring_index][key_index]:
            continue
        dp[ring_index][key_index] = steps
        
        right_index = ring_index + 1
        if right_index == len(ring):
            right_index = 0
        heapq.heappush(heap, (steps+1, right_index, key_index))
        
        left_index = ring_index - 1
        if left_index == -1:
            left_index = len(ring)-1
        heapq.heappush(heap, (steps+1, left_index, key_index))
    return -1