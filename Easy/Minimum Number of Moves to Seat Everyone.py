# Minimum Number of Moves to Seat Everyone
# O(n log n), O(n)
def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    res = 0
    seats.sort()
    students.sort()
    for i in range(len(seats)):
        res += abs(seats[i]-students[i])
    return res

# O(n), O(n)
def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    maxN = max(seats + students)
    arr = [0] * maxN
    for s in seats:
        arr[s-1] += 1
    for s in students:
        arr[s-1] -= 1
    moves = 0
    unmated = 0
    for n in arr:
        moves += abs(unmated)
        unmated += n

    return moves
