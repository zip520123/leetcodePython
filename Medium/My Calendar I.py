# My Calendar I
# O(n log n), O(n)
class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        arr = sorted(self.arr + [(start, end)])
        for i in range(len(arr)-1):
            left_start, left_end = arr[i]
            right_start, right_end = arr[i+1]
            if left_end > right_start:
                return False
        self.arr = arr
        return True

# O(n), O(n)
class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        if not self.arr:
            self.arr.append((start,end))
            return True
        l, r = 0, len(self.arr)
        while l<r:
            mid = l+((r-l)>>1)
            if self.arr[mid] < (start, end):
                l = mid + 1
            else:
                r = mid
        insert_index = l
        prev_index = l-1
        
        if insert_index == 0:
            if end <= self.arr[insert_index][0]:
                self.arr.insert(0, (start, end))
                return True
        if insert_index == len(self.arr):
            if self.arr[prev_index][1] <= start:
                self.arr.append((start, end))
                return True
        if self.arr[prev_index][1] <= start and end <= self.arr[insert_index][0]:
            self.arr.insert(insert_index, (start, end))
            return True
        
        return False