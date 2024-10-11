# The Number of the Smallest Unoccupied Chair
# O(n log n), O(n)
def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    curr_chair = 0
    heap = []
    friend_on_chair = {}
    timeline_set = set()
    start_memo = defaultdict(list)
    end_memo = defaultdict(list)
    for i in range(len(times)):
        start, end = times[i]
        timeline_set.add(start)
        timeline_set.add(end)
        start_memo[start].append(i)
        end_memo[end].append(i)
    timeline = sorted(timeline_set)
    for time in timeline:
        for friend in end_memo[time]:
            chair = friend_on_chair[friend]
            friend_on_chair[friend] = None
            heapq.heappush(heap, chair)
        for friend in start_memo[time]:
            if heap:
                chair = heapq.heappop(heap)
                friend_on_chair[friend] = chair
            else:
                friend_on_chair[friend] = curr_chair
                curr_chair += 1
            if friend == targetFriend:
                return friend_on_chair[friend]

    return -1