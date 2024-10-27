# Task Scheduler
# O(n log n), O(n)
def leastInterval(self, tasks: List[str], n: int) -> int:
    
    heap = []
    memo = defaultdict(int)
    for t in tasks:
        memo[t] += 1
    for key, val in memo.items():
        heapq.heappush(heap, (-val, key))
    arr = []
    cooldown = {}
    time = 0
    while heap or cooldown:
        if time in cooldown:
            heapq.heappush(heap, cooldown.pop(time))
        time += 1
        if heap:
            curr = heapq.heappop(heap)
            count, task = -curr[0], curr[1]
            arr.append(task)
            count -= 1
            if count:
                cooldown[time+n] = (-count, task)
        else:
            arr.append("")

    return len(arr)