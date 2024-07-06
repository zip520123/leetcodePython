# Pass the Pillow
# O(1), O(1)
def passThePillow(self, n: int, time: int) -> int:
    last_time = time % (n - 1)
    round_time = time // (n - 1)
    if round_time % 2 == 0:
        return 1 + last_time
    return n - last_time