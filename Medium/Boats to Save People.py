# Boats to Save People
# O(n log n), O(n)
def numRescueBoats(self, people: List[int], limit: int) -> int:
    people.sort()
    res = 0
    l, r = 0, len(people)-1
    while l<=r:
        res += 1
        if people[l] + people[r] > limit:
            r -= 1
        else:
            r -= 1
            l += 1
    return res