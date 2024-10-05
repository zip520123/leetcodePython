# My Calendar II
# O(n^2), O(n)
class MyCalendarTwo:

    def __init__(self):
        self.start_memo = defaultdict(int)
        self.end_memo = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.start_memo[start] += 1
        self.end_memo[end] += 1
        time_set = set()
        for start_time in self.start_memo.keys():
            time_set.add(start_time)
        for end_time in self.end_memo.keys():
            time_set.add(end_time)
        arr = sorted(time_set)
        count = 0
        for t in arr:
            count += self.start_memo[t]
            count -= self.end_memo[t]
            if count >= 3:
                self.start_memo[start] -= 1
                self.end_memo[end] -= 1
                return False
        return True