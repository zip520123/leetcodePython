# Reverse Words in a String III
# O(n), O(1)
def reverseWords(self, s: str) -> str:
    arr = s.split(" ")
    res = " ".join(list(map(lambda w: w[::-1], arr)))
    return res