# Count Days Without Meetings
# O(n log n) time complexity, O(n) space complexity
def countDays(self, days: int, meetings: List[List[int]]) -> int:
    meetings.sort()
    arr = []
    for i in range(len(meetings)):
        if len(arr) == 0:
            arr.append(meetings[i])
        else:
            if arr[-1][1] >= meetings[i][0]:
                arr[-1][1] = max(arr[-1][1], meetings[i][1])
            else:
                arr.append(meetings[i])
    start = 1
    days_without_meetings = 0

    for i in range(len(arr)):
        gap = arr[i][0] - start
        days_without_meetings += gap
        start = arr[i][1] + 1
    days_without_meetings += days - start + 1

    return days_without_meetings