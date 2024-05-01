# Reverse Prefix of Word
# O(n), O(n)
def reversePrefix(self, word: str, ch: str) -> str:
    for i in range(len(word)):
        if word[i] == ch:
            l, r = 0, i
            arr = list(word)
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return "".join(arr)
    return word