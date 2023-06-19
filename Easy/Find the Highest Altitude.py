# Find the Highest Altitude
# O(n), O(1)
def largestAltitude(self, gain: List[int]) -> int:
    curr = 0; res = 0
    for n in gain:
        curr += n
        res = max(res, curr)
    return res