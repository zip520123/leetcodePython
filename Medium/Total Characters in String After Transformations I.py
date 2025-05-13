# Total Characters in String After Transformations I
# O(size(s) * t), O(1)
def lengthAfterTransformations(self, s: str, t: int) -> int:
    res = 0
    cnt = [0] * 26
    for char in s:
        cnt[ord(char)-ord("a")] += 1
    
    for _ in range(t):
        nxt = [0] * 26
        nxt[0] = cnt[25]
        nxt[1] = (cnt[25] + cnt[0])
        for i in range(2, 26):
            nxt[i] = cnt[i-1]
        cnt = nxt
    return sum(cnt) % (10**9 + 7)